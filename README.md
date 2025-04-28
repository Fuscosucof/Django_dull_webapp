# Rabye_Tuuk

Plan
Article app นั้นเเหละ เเต่ทำเอง ดูref นิดหน่อย

App ที่สามารถ มาพิมหัวข้อเเละcontext ลงเเละให้ผู้อื่นมาcomment ได้
Main point
1) post get edit delete ได้ตามAuthorization ที่ควร
2) 2)ระบบ registration login logout, authorization การเข้าถึงcontent กำหนดในview
3) commments model

Apps: accounts, articles
Steps for accounts app

Steps for pages app appearing all articles
1) startapp, include it in project settings, include in project urls, doing with pages urls and views




Steps for article app
1) start app and add it to settings.py and add TIME_ZONE ="" at the end of file
2) create article model with title body author as foreignkey models.ForeignKey settings.AUTH_USER_MODEL which on_delete=models.CASCADE and have a get_absolute_url(self): function in the model to return each article by its primary key(pk)
3) regis model to admin
4) migrate
5) configure the articleview in admin page by having list_display = [] in ArticleAdmin(admin.ModelAdmin) model
6) update project's urls and views
   urls: for admin/, accounts/, articles/

