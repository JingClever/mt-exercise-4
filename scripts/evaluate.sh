#! /bin/bash

scripts=$(dirname "$0")
base=$scripts/..

data=$base/data_word_level
configs=$base/configs

translations=$base/translations

mkdir -p $translations

src=it
trg=en


num_threads=4
device=0

# measure time

SECONDS=0

# model_name=transformer_word_config
# model_name=transformer_bpe_2k_config
model_name=transformer_bpe_3k_config
beam_size=12

echo "###############################################################################"
echo "model_name $model_name"

translations_sub=$translations/$model_name.$beam_size

mkdir -p $translations_sub

CUDA_VISIBLE_DEVICES=$device OMP_NUM_THREADS=$num_threads python -m joeynmt translate $configs/$model_name.yaml < $data/test.$src > $translations_sub/test.$model_name.$beam_size.$trg

# compute case-sensitive BLEU 

cat $translations_sub/test.$model_name.$beam_size.$trg | sacrebleu $data/test.$trg


echo "time taken:"
echo "$SECONDS seconds"
