//! Cross-port image helpers adapted from iOSPlus10's `tools/op10tool`.
//! Device-specific `ctl`, `bootlog`, and OnePlus UEFI `portpatch` commands are intentionally omitted.

mod im4p;
mod img2simg;
mod ipsw;
mod uefi;

use anyhow::Result;
use clap::{Parser, Subcommand};
use std::path::PathBuf;

#[derive(Parser)]
#[command(name = "portsmith-image-tools", version, about = "Cross-port image and firmware helpers")]
struct Cli {
    #[command(subcommand)]
    command: Command,
}

#[derive(Subcommand)]
#[command(rename_all = "kebab-case")]
enum Command {
    /// Convert a raw image to Android sparse format (4 KiB blocks; preserve allocated HFS+ zero blocks).
    Img2simg { input: PathBuf, output: PathBuf },
    /// Convert an Android sparse image to a raw image.
    Simg2img { input: PathBuf, output: PathBuf },
    /// Read an HFS+ volume size; with --trim, truncate a raw image to that size.
    HfsSize { input: PathBuf, #[arg(long)] trim: bool },
    /// Download named members from a remote ZIP (for example an IPSW) using resumable HTTP range requests.
    IpswGet {
        url: String,
        outdir: PathBuf,
        names: Vec<String>,
        #[arg(short = 'j', long, default_value_t = 32)]
        jobs: usize,
        #[arg(long, default_value_t = 32)]
        chunk_mib: u64,
    },
    /// Unpack UEFI firmware volumes and FFS sections into OUTDIR.
    UefiUnpack { image: PathBuf, outdir: PathBuf },
    /// Extract the payload from an Apple IM4P container (raw or LZFSE-compressed).
    Im4p { input: PathBuf, output: PathBuf },
}

fn main() -> Result<()> {
    match Cli::parse().command {
        Command::Img2simg { input, output } => img2simg::img2simg(&input, &output),
        Command::Simg2img { input, output } => img2simg::simg2img(&input, &output),
        Command::HfsSize { input, trim } => img2simg::hfs_size(&input, trim),
        Command::IpswGet { url, outdir, names, jobs, chunk_mib } => {
            ipsw::run(&url, &outdir, &names, jobs, chunk_mib << 20)
        }
        Command::UefiUnpack { image, outdir } => uefi::run(&image, &outdir),
        Command::Im4p { input, output } => im4p::run(&input, &output),
    }
}
