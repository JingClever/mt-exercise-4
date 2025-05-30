#! /bin/bash

scripts=$(dirname "$0")
base=$scripts/..

data=$base/data

# # # make a new dir to save cutted data
# mkdir -p $data/it_en_raw

# # cut parallel data to 100k lines
# head -n 100000 $data/train.it-en.en > $data/it_en_raw/train.en
# head -n 100000 $data/train.it-en.it > $data/it_en_raw/train.it


# mkdir -p $base/data_word_level

# # preprocess the data with tokenization
# python $base/scripts/preprocess.py \
#     --src $base/data/it_en_raw/train.it \
#     --tgt $base/data/it_en_raw/train.en \
#     --output-src $base/data_word_level/train.it \
#     --output-tgt $base/data_word_level/train.en \
#     --src-lang it \
#     --tgt-lang en \

# python $base/scripts/preprocess.py \
#     --src $base/data/dev.it-en.it \
#     --tgt $base/data/dev.it-en.en \
#     --output-src $base/data_word_level/dev.it \
#     --output-tgt $base/data_word_level/dev.en \
#     --src-lang it \
#     --tgt-lang en \

# python $base/scripts/preprocess.py \
#     --src $base/data/test.it-en.it \
#     --tgt $base/data/test.it-en.en \
#     --output-src $base/data_word_level/test.it \
#     --output-tgt $base/data_word_level/test.en \
#     --src-lang it \
#     --tgt-lang en \


# create BPE codes_3200 and vocabulary files.
# subword-nmt learn-joint-bpe-and-vocab \
#   --input $base/data_word_level/train.it $base/data_word_level/train.en \
#   -s 3200 \
#   -o $base/data_word_level/codes3200.bpe \
#   --write-vocabulary \
#     $base/data_word_level/vocab_3200.it.raw \
#     $base/data_word_level/vocab_3200.en.raw

# cat $base/data_word_level/train.it $base/data_word_level/train.en \
#   | subword-nmt apply-bpe -c $base/data_word_level/codes3200.bpe \
#   | subword-nmt get-vocab \
#   > $base/shared_models/joint-vocab_3200.raw


# cut -d ' ' -f1 $base/shared_models/joint-vocab3200.raw \
#   > $base/shared_models/joint-vocab_3200.txt

mkdir -p $base/results
python $base/scripts/draw_graphs.py -i $base/result.txt -o $base/results/beam_bleu_time.png