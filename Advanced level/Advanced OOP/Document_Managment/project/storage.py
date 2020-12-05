class Storage:

    def __init__(self):

        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: 'Category'):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: 'Topic'):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: 'Document'):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name:str ):
        e_category = [c for c in self.categories if category_id == c.id][0]
        e_category.name = new_name


    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        e_topic = [t for t in self.topics if topic_id == t.id][0]
        e_topic.name = new_topic
        e_topic.storage_folder = new_storage_folder

    def edin_document(self, document_id: int, new_file_name: str):
        e_document = [d for d in self.documents if document_id == d.id][0]
        e_document.file_name = new_file_name

    def delete_category(self,category_id):
        del_category = [c for c in self.categories if category_id == c.id][0]
        self.categories.remove(del_category)

    def delete_topic(self, topic_id):
        del_topic = [t for t in self.topics if topic_id == t.id][0]
        self.categories.remove(del_topic)

    def delete_document(self, document_id):
        del_document = [d for d in self.documents if document_id == d.id][0]
        self.categories.remove(del_document)

    def get_document(self, document_id):
        document = [d for d in self.documents if document_id ==d.id][0]
        return document


    def __repr__(self):
        document = list(map(str, self.documents))
        return '\n'.join(document)