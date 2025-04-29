# Rabye_Tuuk

article apps routemap

$$1) article model มีattr :title body date author(Foreignkey)
โดยมี get_absolute_url เพื่อเป็น url ในการDetailView article individually ตามpk
เเบ้วเอาลงAdmin
$$2) ทำให้ Show article ในadmin มีlist_display เเต่ละ attr
$$3) ทำ ListView DetailView ปล. list ของmodel คือ ชื่อ model ตัวพิมเล็ก_list
model = Article ดังนั้น model_list = article_list
4) ใส่ <a></a> สำหรับ edit delete ไว้เปล่าๆก่อน
$$5)  UpdateView DeleteView จาก django.views.generic.edit
- UpdateView ใส่ fields ที่ต้องการที่จะให้updateได้
- DeleteView ใส่ success_url = reverse_lazy ("url name") ไว้ด้วย
6) Template ของเเต่ละอัน ใช้ {{object.}} หรือ {{article.}} dHwfh
ุุุ- template ของ edit มี {{form}} build in เหมือนเดิม
- template ของ delete ไม่ต้องมี {{form}} นะถถถ มีเเค่<form action='' method='post'><button></button></form>
7) กลับไปใส่ชื่อ url ของ edit กับ delete {% url 'name' article.pk %}
8) ทำ CreateView ระบุ fields เเล้วทำtemplate เเล้วใส่ชื่อ url ใน base.html
ละก็ link ไปหน้า listview จากหน้า home

Permission ในการ CRUD