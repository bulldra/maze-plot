# 概要

迷路の最善手を方策勾配法で学習  
学習結果のアニメーションgifを生成する

[解説記事](https://www.du-soleil.com/entry/maze-lerning)  
参考図書：[つくりながら学ぶ! 深層強化学習 PyTorchによる実践プログラミング](https://www.amazon.co.jp/exec/obidos/ASIN/4839965625/bulldra-22/)

## ビルド

```bash
docker-compose build
```

## 実行

```bash
docker-compose run --entrypoint "python3 /data/src/main.py" maze-plot
```

work フォルダ内に生成された迷路・学習前・学習後の画像を出力

## 学習前

![学習前](/sample/input.gif)

## 学習後

![学習後](/sample/result.gif)
