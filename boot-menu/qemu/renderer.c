#include <stdint.h>
#include "scene.h"

#define FB_BASE 0x9c000000UL
static volatile uint32_t *const fb = (volatile uint32_t *)FB_BASE;

static const uint8_t font[36][7] = {
    {14,17,17,31,17,17,17}, {30,17,17,30,17,17,30}, {14,17,16,16,16,17,14},
    {30,17,17,17,17,17,30}, {31,16,16,30,16,16,31}, {31,16,16,30,16,16,16},
    {14,17,16,23,17,17,15}, {17,17,17,31,17,17,17}, {14,4,4,4,4,4,14},
    {7,2,2,2,18,18,12}, {17,18,20,24,20,18,17}, {16,16,16,16,16,16,31},
    {17,27,21,21,17,17,17}, {17,25,21,19,17,17,17}, {14,17,17,17,17,17,14},
    {30,17,17,30,16,16,16}, {14,17,17,17,21,18,13}, {30,17,17,30,20,18,17},
    {15,16,16,14,1,1,30}, {31,4,4,4,4,4,4}, {17,17,17,17,17,17,14},
    {17,17,17,17,17,10,4}, {17,17,17,21,21,21,10}, {17,17,10,4,10,17,17},
    {17,17,10,4,4,4,4}, {31,1,2,4,8,16,31},
    {14,17,19,21,25,17,14}, {4,12,4,4,4,4,14}, {14,17,1,2,4,8,31},
    {30,1,1,14,1,1,30}, {2,6,10,18,31,2,2}, {31,16,16,30,1,1,30},
    {14,16,16,30,17,17,14}, {31,1,2,4,8,8,8}, {14,17,17,14,17,17,14},
    {14,17,17,15,1,1,14}
};

static uint32_t rgb(uint32_t c) { return 0xff000000u | (c & 0x00ffffffu); }
static uint32_t mix(uint32_t a, uint32_t b, unsigned t)
{
    unsigned r1=(a>>16)&255,g1=(a>>8)&255,b1=a&255;
    unsigned r2=(b>>16)&255,g2=(b>>8)&255,b2=b&255;
    unsigned r=(r1*(255-t)+r2*t)/255,g=(g1*(255-t)+g2*t)/255,bb=(b1*(255-t)+b2*t)/255;
    return 0xff000000u | r<<16 | g<<8 | bb;
}
static void clear(uint32_t color)
{
    for (int y=0; y<SCENE_HEIGHT; y++) {
        volatile uint32_t *row=fb+y*SCENE_WIDTH;
        for (int x=0; x<SCENE_WIDTH; x++) row[x]=color;
    }
}
static int inside_round(int x,int y,int w,int h,int radius)
{
    int cx=x<radius?radius:x>=w-radius?w-radius-1:x;
    int cy=y<radius?radius:y>=h-radius?h-radius-1:y;
    int dx=x-cx,dy=y-cy;
    return dx*dx+dy*dy<=radius*radius;
}
static void round_rect(int x,int y,int w,int h,int r,uint32_t c)
{
    for(int yy=0;yy<h;yy++){
        if(y+yy<0||y+yy>=SCENE_HEIGHT)continue;
        volatile uint32_t *row=fb+(y+yy)*SCENE_WIDTH;
        for(int xx=0;xx<w;xx++)
            if(x+xx>=0&&x+xx<SCENE_WIDTH&&inside_round(xx,yy,w,h,r))row[x+xx]=c;
    }
}
static void draw_gradient(int x,int y,int size,uint32_t c1,uint32_t c2)
{
    int r=size/5;
    for(int yy=0;yy<size;yy++){
        if(y+yy<0||y+yy>=SCENE_HEIGHT)continue;
        volatile uint32_t *row=fb+(y+yy)*SCENE_WIDTH;
        for(int xx=0;xx<size;xx++){
            if(x+xx<0||x+xx>=SCENE_WIDTH||!inside_round(xx,yy,size,size,r))continue;
            unsigned t=(unsigned)(xx+yy)*255u/(unsigned)(2*(size-1));
            row[x+xx]=mix(c1,c2,t);
        }
    }
}
static void glyph(char c,uint8_t out[7])
{
    if(c>='a'&&c<='z')c-=32;
    if(c>='A'&&c<='Z'){
        const uint8_t *g=font[c-'A'];for(int i=0;i<7;i++)out[i]=g[i];return;
    }
    if(c>='0'&&c<='9'){
        const uint8_t *g=font[26+c-'0'];for(int i=0;i<7;i++)out[i]=g[i];return;
    }
    for(int i=0;i<7;i++)out[i]=0;
}
static int text_width(const char *s,int scale){int n=0;while(s[n])n++;return n*6*scale-scale;}
static void text(int x,int y,int scale,const char *s,uint32_t color)
{
    for(;*s;s++,x+=6*scale){uint8_t rows[7];glyph(*s,rows);
        for(int gy=0;gy<7;gy++)for(int gx=0;gx<5;gx++)if(rows[gy]&(1u<<(4-gx)))
            for(int sy=0;sy<scale;sy++)for(int sx=0;sx<scale;sx++){
                int px=x+gx*scale+sx,py=y+gy*scale+sy;
                if(px>=0&&px<SCENE_WIDTH&&py>=0&&py<SCENE_HEIGHT)fb[py*SCENE_WIDTH+px]=color;
            }
    }
}
static void text_center(int center_x,int y,int scale,const char *s,uint32_t color)
{ text(center_x-text_width(s,scale)/2,y,scale,s,color); }
static void draw_icon(const struct preview_entry *e,int x,int y,int size)
{
    draw_gradient(x,y,size,e->icon_start,e->icon_end);
    int scale=size/23;if(scale<2)scale=2;
    text_center(x+size/2,y+size/2-4*scale,scale,e->icon_text,0xffffffffu);
}
static void draw_stack(void)
{
    int content_top=SCENE_HEIGHT*13/100,content_bottom=SCENE_HEIGHT*90/100;
    int slot=(content_bottom-content_top)/SCENE_COUNT;
    int label_h=slot*8/100,gap=slot*6/100;
    int size=slot-label_h-gap;
    if(size>SCENE_WIDTH*40/100)size=SCENE_WIDTH*40/100;
    int row_h=size+label_h+gap;
    int total=SCENE_COUNT*row_h-gap;
    int y=content_top+(content_bottom-content_top-total)/2;
    for(int i=0;i<SCENE_COUNT;i++){
        const struct preview_entry *e=&scene_entries[i];
        int x=(SCENE_WIDTH-size)/2,iy=y+i*row_h;
        if(i==SCENE_SELECTED)round_rect(x-16,iy-16,size+32,size+32,size/5+16,SCENE_SELECTION);
        draw_icon(e,x,iy,size);
        text_center(SCENE_WIDTH/2,iy+size+8,5,e->label,e->enabled?SCENE_TEXT:SCENE_DISABLED);
    }
}
static void draw_list(void)
{
    int margin=SCENE_WIDTH*10/100;
    int content_top=SCENE_HEIGHT*15/100,content_bottom=SCENE_HEIGHT*88/100;
    int content_height=content_bottom-content_top;
    int row_h=content_height*68/(100*SCENE_COUNT/1);
    int gap=content_height*10/(100*SCENE_COUNT/1);
    int total=SCENE_COUNT*row_h+(SCENE_COUNT-1)*gap;
    int y=content_top+(content_height-total)/2;
    for(int i=0;i<SCENE_COUNT;i++){
        const struct preview_entry *e=&scene_entries[i];int yy=y+i*(row_h+gap);
        if(i==SCENE_SELECTED)round_rect(margin-10,yy-10,SCENE_WIDTH-2*margin+20,row_h+20,24,SCENE_SELECTION);
        round_rect(margin,yy,SCENE_WIDTH-2*margin,row_h,18,SCENE_SURFACE);
        text(margin+row_h/5,yy+row_h/3,6,e->label,e->enabled?SCENE_TEXT:SCENE_DISABLED);
        text(margin+row_h/5,yy+row_h*2/3,3,e->detail,SCENE_SECONDARY);
    }
}
static void draw_cards(void)
{
    int cols=SCENE_WIDTH*10/SCENE_HEIGHT>11?3:2;
    if(SCENE_WIDTH*100/SCENE_HEIGHT<65)cols=1;
    int margin=SCENE_WIDTH*6/100,gap=SCENE_WIDTH*3/100;
    int card_w=(SCENE_WIDTH-2*margin-(cols-1)*gap)/cols;
    int content_top=SCENE_HEIGHT*16/100,content_bottom=SCENE_HEIGHT*88/100;
    int rows=(SCENE_COUNT+cols-1)/cols;
    int card_h=(content_bottom-content_top-(rows-1)*SCENE_HEIGHT*3/100)/rows;
    if(card_h>SCENE_HEIGHT*25/100)card_h=SCENE_HEIGHT*25/100;
    int total=rows*card_h+(rows-1)*gap;
    int y=content_top+((content_bottom-content_top)-total)/2;
    for(int i=0;i<SCENE_COUNT;i++){
        const struct preview_entry *e=&scene_entries[i];int row=i/cols,col=i%cols;
        int x=margin+col*(card_w+gap),yy=y+row*(card_h+gap);
        if(i==SCENE_SELECTED)round_rect(x-10,yy-10,card_w+20,card_h+20,24,SCENE_SELECTION);
        round_rect(x,yy,card_w,card_h,20,SCENE_SURFACE);
        int icon_size=card_h*45/100,icon_x=x+card_h/8,icon_y=yy+(card_h-icon_size)/2;
        draw_icon(e,icon_x,icon_y,icon_size);
        int tx=icon_x+icon_size+card_h/8;
        text(tx,yy+card_h/2-18,5,e->label,e->enabled?SCENE_TEXT:SCENE_DISABLED);
        text(tx,yy+card_h/2+28,3,e->detail,SCENE_SECONDARY);
    }
}
void render_menu(void)
{
    clear(SCENE_BG);
    int title_scale=SCENE_WIDTH/110;
    if(title_scale<2)title_scale=2;
    text_center(SCENE_WIDTH/2,SCENE_HEIGHT*6/100,title_scale,SCENE_TITLE,SCENE_TEXT);
    if(SCENE_LAYOUT==0)draw_stack();else if(SCENE_LAYOUT==1)draw_list();else draw_cards();
    int footer_scale=SCENE_WIDTH/300;if(footer_scale<1)footer_scale=1;
    text_center(SCENE_WIDTH/2,SCENE_HEIGHT-SCENE_HEIGHT*4/100,footer_scale,"QEMU PREVIEW ONLY - NO BOOT ACTION",SCENE_SECONDARY);
}
