#!/usr/bin/env bash

set -euo pipefail

# See the name conventions from:
# https://data.cma.cn/article/showPDFFile.html?file=/pic/static/doc/F/CLDAS-V2.0/CLDAS-V2.0_ADP.pdf

readonly prefix_length=29

dry_run=false
target_dir=.

usage() {
	printf 'Usage: %s [-n|--dry-run] [directory]\n' "${0##*/}"
}

while (($# > 0)); do
	case "$1" in
		-n|--dry-run)
			dry_run=true
			shift
			;;
		-h|--help)
			usage
			exit 0
			;;
		--)
			shift
			break
			;;
		-*)
			printf 'Unknown option: %s\n' "$1" >&2
			usage >&2
			exit 1
			;;
		*)
			if [[ "$target_dir" != . ]]; then
				printf 'Only one directory argument is supported\n' >&2
				usage >&2
				exit 1
			fi

			target_dir=$1
			shift
			;;
	esac
done

if (($# > 0)); then
	printf 'Unexpected arguments: %s\n' "$*" >&2
	usage >&2
	exit 1
fi

if [[ ! -d "$target_dir" ]]; then
	printf 'Directory not found: %s\n' "$target_dir" >&2
	exit 1
fi

shopt -s nullglob

cd -- "$target_dir"

for source_name in *Z_NAFP*; do
	trimmed_name=${source_name%%\?*}

	if (( ${#trimmed_name} <= prefix_length )); then
		printf 'Skipping %s: filename is shorter than expected after trimming\n' "$source_name" >&2
		continue
	fi

	target_name=${trimmed_name:prefix_length}

	if [[ "$source_name" == "$target_name" ]]; then
		printf 'Skipping %s: no rename needed\n' "$source_name"
		continue
	fi

	if [[ -e "$target_name" ]]; then
		printf 'Skipping %s: target already exists: %s\n' "$source_name" "$target_name" >&2
		continue
	fi

	if [[ "$dry_run" == true ]]; then
		printf 'Would rename %s -> %s\n' "$source_name" "$target_name"
		continue
	fi

	printf 'Renaming %s -> %s\n' "$source_name" "$target_name"
	mv -- "$source_name" "$target_name"
done
