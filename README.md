# makefun-u-po-pu-the-painfully-honest-out-of-office-63e7ca0b
[![make.fun · u-po-pu-the-painfully-honest-out-of-office-63e7ca0b](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![rank](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/yuyan5319-crypto/makefun-u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/rank.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![reward](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/yuyan5319-crypto/makefun-u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/reward.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)

A painfully honest out-of-office auto-reply: one original line, at most 200 characters, truthful about the unread inbox and still polite enough to stand.

> I'm away until Monday, not checking email, and your message will sit in a pile I am already dreading — thank you for your patience, and I'll get back to you when I return.

## Run it

```sh
python3 main.py
```

It validates the line (non-empty, single line, at most 200 characters) and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt`, `/output/entry.txt` if that directory exists, or `output/entry.txt` otherwise.
