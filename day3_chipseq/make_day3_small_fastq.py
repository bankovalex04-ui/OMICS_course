import gzip
from pathlib import Path

FULL = Path("/mnt/d/omics_course/OMICS_course_spring_2026/day3_ChIPseq_practice")
SMALL = Path("/mnt/d/omics_course/OMICS_course_spring_2026/day3_ChIPseq_practice_small")

N_PAIRS = 1_000_000
N_LINES = N_PAIRS * 4

samples = [
    "MoPh7_H3K9me3",
    "MoPh7_input",
    "MoPh7_H3K27Ac",
    "MoPh7_H2A119Ub",
    "MoPh7_CTCF",
    "MoPh7_CTCF_input",
]

for sample in samples:
    outdir = SMALL / "data" / "raw" / sample
    outdir.mkdir(parents=True, exist_ok=True)

    for read in ["R1", "R2"]:
        src = FULL / "data" / "raw" / sample / f"{sample}_{read}.fastq.gz"
        dst = outdir / f"{sample}_{read}.fastq.gz"

        print(f"subsampling {sample} {read}")
        with gzip.open(src, "rb") as fin, gzip.open(dst, "wb", compresslevel=6) as fout:
            for i, line in enumerate(fin):
                if i >= N_LINES:
                    break
                fout.write(line)

print("done")
