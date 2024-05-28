class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    
    

class Author:
    def __init__(self, name):
        self._name = name 
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all if article.author == self]
        

    def magazines(self):
        return list(set(article.magazine for article in Article.all if article.author == self))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
       categories = {article.magazine.category for article in Article.all if article.author == self}
       return list(categories) if categories else None
    



class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not isinstance(category, str):
            raise ValueError("Category must be a string")
        if not 2 <= len(name) <= 16:
            raise ValueError("Name must be between 2 and 16 characters long")
        if not category:
            raise ValueError("Category cannot be empty")
        
        self.name = name
        self.category = category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in Article.all if article.magazine == self))

    def article_titles(self):
        titles = [article.title for article in Article.all if article.magazine == self]
        return titles or None

    def contributing_authors(self):
        author_article_count = {}
        for article in self.articles():
            author_name = article.author.name
            author_article_count[author_name] = author_article_count.get(author_name, 0) + 1
        return [author for author in set(article.author for article in self.articles()) 
                if author_article_count.get(author.name, 0) > 2]