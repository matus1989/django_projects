from django.contrib import admin
from .models import Author, Genre,Language, Book, BookInstance
# Register your models here.

admin.site.register(Genre)
admin.site.register(Language)

class BooksInsanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

class BookInline(admin.TabularInline):
    model = Book 
    extra = 0

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name','date_of_birth','date_of_death')
    fields = ['first_name','last_name',('date_of_birth', 'date_of_death')]
    inlines = [BookInline]
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','display_genre','language')
    
    inlines = [BooksInsanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','imprint','status','due_back','id')
    
    list_filter = ('status','due_back')
    
    fieldsets = (
        (None, {
            "fields": (
               'book',
               'imprint',
               'id' 
            ),
        }),
        
        ('Availability',{
            'fields':('status','due_back')
        }),
    )
    
