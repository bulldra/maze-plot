# 概要

迷路の最善手を方策勾配法で学習  
学習結果のアニメーションgifを生成する

[解説記事](https://www.du-soleil.com/entry/maze-lerning)

## ビルド

```bash
docker-compose build
```


## 実行

```bash
docker-compose run --entrypoint "python3 /data/src/main.py" maze-plot
```

work フォルダ内に生成された迷路・学習前・学習後の画像を出力

![結果例](./sample.jpg)
