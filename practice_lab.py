class Movie:
    def __init__(self, name, year, director, box_office):
        self.name = name
        self.year = year
        self.director = director
        self.box = box_office
    
    def box_office(self):
        ## 我的寫法
        total_box = int()
        for i in range(len(self.box)):
            total_box += self.box[i]
        return '$' + str(total_box) +' millions'
        
        ## 簡潔快速寫法
        # return "$%d millions" % sum(self.box)

    def is_earlier_than(self, other):
        ## 我的寫法
        if self.year < other.year:
            return True
        else:
            return False
        
        ## 簡潔快速寫法
        # return self.year < other.year


frozen = Movie('Frozen', 2013, 'Jennifer', [1000, 200])
lionKing = Movie('Lion King', 1994, 'Robert Ralph', [4000, 500])
# print(frozen.year) # 2013
# print(frozen.box) # [1000, 200]


print(frozen.box_office()) # $1200 millions
print(frozen.is_earlier_than(lionKing)) # False