class Keyword:
    def __init__(self, name, value, rank, major):
        self.name = name
        self.value = value
        self.rank = rank
        self.major = major

class AssociatedTheme:
    def __init__(self, name, numofoccurences):
        self.name = name
        self.numofoccurences = numofoccurences

        
class Author:
    def __init__(self, firstname, lastname, organization, rank):
        self.firstname = firstname
        self.lastname = lastname
        self.organization = organization
        self.rank = rank

class Article:
    def __init__(self,
                snippet,
                lead_paragraph,
                source,
                keywords,
                pub_date,
                document_type,
                news_desk,
                section_name,
                authors,
                type_of_material,
                word_count):
        self.snippet = snippet
        self.lead_paragraph = lead_paragraph
        self.source = source
        self.keywords = keywords
        self.pub_date = pub_date
        self.document_type = document_type
        self.news_desk = news_desk
        self.section_name = section_name
        self.authors = authors
        self.type_of_material = type_of_material
        self.word_count = word_count

class Article_reduced:
    def __init__(self,
                snippet,
                web_url,
                source,
                pub_date,
                document_type,
                news_desk,
                section_name,
                type_of_material,
                word_count,
                print_section,
                print_page):
        self.snippet = snippet,
        self.web_url = web_url,
        self.source = source,
        self.pub_date = pub_date,
        self.document_type = document_type,
        self.news_desk = news_desk,
        self.section_name = section_name,
        self.type_of_material = type_of_material,
        self.word_count = word_count,
        self.print_section = print_section,
        self.print_page = print_page    

    def to_dict(self):
        return {
            'snippet': self.snippet,
            'web_url': self.web_url,
            'source': self.source,
            'pub_date': self.pub_date,
            'document_type': self.document_type,
            'news_desk': self.news_desk,
            'section_name': self.section_name,
            'type_of_material': self.type_of_material,
            'word_count': self.word_count,
            'print_section': self.print_section,
            'print_page': self.print_page,
        }