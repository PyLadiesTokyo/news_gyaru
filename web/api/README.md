# WEB API

## サイトカテゴリ取得

送付されたURLに対応したカテゴリを取得する。   
本システムが対応していないサイトの場合はcategory返却されません。

### input

- [domain]/url
- POST
- body:JSON
  - url(String)
  
```json
{
  "url" : "http://xxxx.co.jp/foo/1234bar.html"
}

```

### output

- JSON
  - category(String)
  - url(String)

```json
{
  "category": "news",
  "url": "http://xxxx.co.jp/foo/1234bar.html"
}

```

## 文章変換処理

送られてきた文章をギャル語に変換する。   

### input

- [domain]/[category]/replace
  - categoryは「サイトカテゴリ取得API」で取得したカテゴリを使用してください
- POST
- body:JSON
  - text(String)
 
```json
{
  "text": "トランプ米大統領は１６日、フロリダ州マイアミで演説し、キューバ政策を変更すると発表した。"
}
```

### output

- JSON
  - replaceText(String)
  
```json
{
  "replaceText": "トランプ氏、１６日にフロリダ州マイアミでべしゃって、キューバさんの政策を変えちゃうとかなんとか言っちゃって〜！"
}
```
  