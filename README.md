# ๐ 1021_pairpjt

> ์ผ์ : 2022-10-21
> 
> ํ ๊ตฌ์ฑ : ๊ฐ์ธ์ ์

## ๐ฅ๏ธ ํ๋ก์ ํธ ์์ฐ



![ezgif-1-83b68b5fd1.gif](assets/a3d523d52db90913b7178dcf57c1616618eee43c.gif)

![ezgif-1-353907e722.gif](assets/d2c508a6671851563b316b3d953a70c79296835b.gif)

## ๐งญ ๋ชฉํ

- **CRUD** ๊ตฌํ
- **Staticfiles** ํ์ฉ ์ ์  ํ์ผ(์ด๋ฏธ์ง, CSS, JS) ๋ค๋ฃจ๊ธฐ
- Django **Auth** ํ์ฉ ํ์ ๊ด๋ฆฌ ๊ตฌํ
- Media ํ์ฉ ๋์  ํ์ผ ๋ค๋ฃจ๊ธฐ
- ๋ชจ๋ธ๊ฐ 1 : N ๊ด๊ณ ๋งคํ ์ฝ๋ ์์ฑ ๋ฐ ํ์ฉ
  - ์ ์  - ๋ฆฌ๋ทฐ
  - ๋ฆฌ๋ทฐ - ๋๊ธ
  - ์ ์  - ๋๊ธ

## โ๏ธ Stacks

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=ffffff"/> <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=ffffff"/> <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=flat-square&logo=Bootstrap&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=Git&logoColor=ffffff"/> <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=ffffff"/>

## ๐งฑ  ๊ธฐ๋ฅ ์๊ฐ

- ๊ตฌํ๋ ๊ธฐ๋ฅ
1. ํ์ ๊ด๋ฆฌ ๊ธฐ๋ฅ
   
   1. ํ์ ๊ฐ์
   2. ํ์ ์ ๋ณด ์์ 
   3. ๋น๋ฐ๋ฒํธ ์์ 
   4. ๋ก๊ทธ์ธ, ๋ก๊ทธ์์
   5. ํ์ ํํด

2. ๊ฒ์๊ธ ๊ธฐ๋ฅ
   
   1. ์ํ ํฌ๋กค๋ง์ ์ด์ฉํ ๊ธฐ์ด ๋ฐ์ดํฐ ์์ฑ
   2. ์ธ๋ํค ์ฐ๊ฒฐ์ ํตํ ๋ฐ์ดํฐ ์ฐ๊ฒฐ
   3. CRUD ๊ธฐ๋ฐ ๊ฒ์ํ ์์คํ 
   4. CKeditor๋ฅผ ํตํ ๊ฒ์๊ธ ์์ฑ
- ๋ฏธ๊ตฌํ๋ ๊ธฐ๋ฅ
1. Ajax๋ฅผ ์ด์ฉํ ๋๊ธ ์ฒ๋ฆฌ ๊ธฐ๋ฅ

## ๐ก๊ฒฝํ ๋ฐ ๋ฏธํกํ ์ 

1. ๊ฒ์ํ์์ ์๋นํ ์์ฃผ ์ฌ์ฉ๋๋ ck์๋ํฐ๋ฅผ ์ด์ฉํด ํ๋ก์ ํธ๋ฅผ ์งํํ์๋ค. 
   - ์ฑ ์ค์น๋ถํฐ ๊ฒฝ๋ก ์ง์ ๊น์ง ์์ฒญ๋๊ฒ ๊ณ ์์ ํ๋๋ฐ ๊ฐ๋ ฅํ ๊ธฐ๋ฅ๋ค์ด ๋ง์ ๋ง์กฑ์ค๋ฌ์. 
2. ck์๋ํฐ์ ์ด๋ฏธ์ง ์๋ก๋ ๊ถํ์ **์คํํ**๋ก๋ง ์ค์ ๋์ด ์๋ค. <br>
   ์ ์  ๋ก๊ทธ์ธ์ ์๋ํ๋๊ฑธ๋ก ๊ฐ์ํ๊ฒฝ์์ ๊ผญ ๋ณ๊ฒฝํด์ผ ํ๋ค.
      ``` python
      #{๊ฐ์ํ๊ฒฝ} /Lib/site-packages/ckeditor_uploader/urls.py
      urlpatterns = [
         re_path(r"^upload/", login_required(views.upload), name="ckeditor_upload"),
         re_path(
            r"^browse/",
            never_cache(login_required(views.browse)),
            name="ckeditor_browse",
         ),
      ]
      ```

3. ๊ฒ์๊ธ ์ญ์ ์ ๊ฒ์๊ธ์ ํฌํจ๋ ์ด๋ฏธ์ง๋ ์ญ์ ํ๋ ๋ฐฉ์๋ ๊ตฌํ์ด ํ์ํ๋ค ์๊ฐํจ. 

