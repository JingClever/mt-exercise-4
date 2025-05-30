import argparse
import re
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

def parse_args():
    parser = argparse.ArgumentParser(
        description="Extract beam_size, BLEU scores, and generation time from a results file and plot them within one PNG."
    )
    parser.add_argument(
        "-i", "--results-file",
        default="results.txt",
        help="Path to the results file"
    )
    parser.add_argument(
        "-o", "--out",
        default="beam_bleu_time.png",
        help="Path to the output PNG file"
    )
    return parser.parse_args()

def extract_runs(text, model_name="transformer_bpe_3k_config"):
    runs = []
    for part in text.split("model_name "):
        if part.startswith(model_name):
            runs.append(part)
    return runs

def parse_run(run):
    beam_re  = re.compile(r"beam_size=(\d+)")
    bleu_re  = re.compile(r'"score":\s*([\d\.]+)')
    time_re1 = re.compile(r"Generation took\s*([\d\.]+)\[sec\]")
    time_re2 = re.compile(r"time taken:\s*([\d\.]+)\s*seconds", re.IGNORECASE)

    bm = beam_re.search(run)
    bl = bleu_re.search(run)
    tm = time_re1.search(run) or time_re2.search(run)

    if not (bm and bl and tm):
        return None

    return {
        "beam": int(bm.group(1)),
        "bleu": float(bl.group(1)),
        "time": float(tm.group(1))
    }

def parse_results_file(path):
    with open(path, "r") as f:
        text = f.read()
    runs = extract_runs(text)
    parsed = [parse_run(r) for r in runs]
    parsed = [p for p in parsed if p is not None]
    parsed.sort(key=lambda x: x["beam"])
    beams = [p["beam"] for p in parsed]
    bleus = [p["bleu"] for p in parsed]
    times = [p["time"] for p in parsed]
    return beams, bleus, times

def plot_combined(beams, bleus, times, out_png,
                  bleu_color="steelblue",
                  time_cmap="viridis_r",
                  bg_color="#f7f7f7"):
    x = np.array(beams)
    y_bleu = np.array(bleus)
    y_time = np.array(times)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6), sharex=True)
    ax1.set_xticks(beams)
    fig.patch.set_facecolor(bg_color)
    ax1.set_facecolor(bg_color)
    ax2.set_facecolor(bg_color)

    ax1.plot(
        x, y_bleu,
        color=bleu_color,
        linewidth=2,
        marker="o",
        markersize=5,
        markeredgecolor="k"
    )
    ax1.set_xlabel("Beam Size")
    ax1.set_ylabel("BLEU Score")
    ax1.set_title("BLEU Score vs. Beam Size")
    ax1.grid(True, color="white")

    pts     = np.stack([x, y_time], axis=1)
    segs    = np.stack([pts[:-1], pts[1:]], axis=1)
    norm    = plt.Normalize(vmin=y_time.min(), vmax=y_time.max())
    lc      = LineCollection(segs, cmap=time_cmap, norm=norm, linewidth=2)
    lc.set_array(y_time[:-1])
    ax2.add_collection(lc)
    sc = ax2.scatter(
        x, y_time,
        c=y_time, cmap=time_cmap, norm=norm,
        s=20, edgecolor="k"
    )
    ax2.set_xlabel("Beam Size")
    ax2.set_ylabel("Time (s)")
    ax2.set_title("Generation Time vs. Beam Size")
    ax2.set_xlim(x.min(), x.max())
    ax2.set_ylim(y_time.min(), y_time.max())
    fig.colorbar(lc, ax=ax2, label="Time (s)")
    ax2.grid(True, color="white")

    plt.tight_layout()
    fig.savefig(out_png)
    plt.show()

def main():
    args = parse_args()
    beams, bleus, times = parse_results_file(args.results_file)
    plot_combined(beams, bleus, times, args.out)

if __name__ == "__main__":
    main()
