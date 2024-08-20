# config for training GPT-2 (124M) down to very nice loss of ~2.85 on 1 node of 8X A100 40GB
# launch as the following (e.g. in a screen session) and wait ~5 days:
# $ torchrun --standalone --nproc_per_node=8 train.py config/train_gpt2.py

wandb_log = True
wandb_project = 'owt'
wandb_run_name='gpt2-124M'

# these make the total batch size be ~0.5M
# 16 batch size * 1024 block size * 5 gradaccum * 2 GPUs = 163,840 [491,520]
# batch_size = 16
batch_size = 10
block_size = 1024
gradient_accumulation_steps = 16 * 2

# this makes total number of tokens be 300B
max_iters = 300000
lr_decay_iters = 300000

# eval stuff
eval_interval = 500
eval_iters = 400
log_interval = 20

# weight decay
weight_decay = 1e-1
