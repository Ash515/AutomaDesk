import os

def get_file_summary(directory):
    summary = {}
    total_files = 0

    for root, _, files in os.walk(directory):
        for filename in files:
            total_files += 1

            if "." in filename:
                extension = filename.rsplit(".", 1)[-1].lower()
            else:
                extension = "no_ext"

            summary[extension] = summary.get(extension, 0) + 1

    return summary, total_files


def display_result(summary, total):
    print("\n File Analysis Report")
    print("-" * 30)
    print(f"Total files scanned: {total}\n")

    for ext, count in sorted(summary.items(), key=lambda x: x[1], reverse=True):
        percentage = (count / total) * 100 if total > 0 else 0
        print(f".{ext:<10} : {count} files ({percentage:.2f}%)")


if __name__ == "__main__":
    folder = input("Enter folder path to analyze: ").strip()

    if not os.path.exists(folder):
        print("Invalid path. Please try again.")
    else:
        result, total = get_file_summary(folder)
        display_result(result, total)