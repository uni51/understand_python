class Person:

    def __init__(self, name):
        self.name = name # name.setterのnameメソッド呼び出し。_nameに格納される

    # @propertyは、プロパティを作成するためのデコレータ
    @property
    def name(self):
        """ self.nameやperson.nameとアクセスすると、このメソッドが呼び出されます """
        return self._name

    # @プロパティ名.setterは、プロパティに値を設定するためのメソッドを定義するためのデコレータ
    @name.setter
    def name(self, value):
        """ self.name=''やperson.name=''で呼び出される。_nameに格納します """       
        if not value:
            value = '名無しの権兵衛'
        self._name = value


person = Person('')
print(person.name)