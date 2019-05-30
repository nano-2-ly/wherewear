class person(object):
    def __init__(self):
        '''
        # class person

        This class contain varialbe information about client.
        Client record detail information about their clothes, and sever would calculate client future state about weather(or cilmate).

        + top_clothes
        This variable contain clothes detail informations(that is clothes_detail_information object) about top clothes.
        'top_clothes' would be list of clothes_detail_informtion object.

        + bottom_clothes
        This variable contain clothes detail informations(that is clothes_detail_information object) about botton clothes.
        'bottom_clothes' would be list of clothes_detail_informtion object.

        + personal_information
        This variable contain personal informations(that is personal_information object).
        'personal_information' would be personal_information object.

        + top_clothes_score
        This varialbe contains result of evaluation about top clothes attributes.

        + bottom_clothes_score
        This variable contains result of evaluation about bottom clothes attributes.

        + personal_information_score
        This variable contains reuslt of evaluation about personal_information attributes


        '''
        
        self.top_clothes = []
        self.bottom_clothes = []
        self.personal_information = None

        self.top_clothes_score = None
        self.bottom_clothes_score = None
        self.personal_information_score = None

    def get_top_clothes(self, top_clothes_item):
        self.top_clothes.append(top_clothes_item)

    def get_bottom_clothes(self, bottom_clothes_item):
        self.bottom_clothes.append(bottom_clothes_item)

    def get_personal_information(self, personal_information):
        self.personal_information = personal_information

    def get_top_clothes_score(self, top_clothes_score):
        self.get_top_clothes_score = top_clothes_score
    
    def get_bottom_clothes_score(self, bottom_clothes_score):
        self.get_bottom_clothes_score = bottom_clothes_score
    
    def get_personal_information_score(self, personal_information_score):
        self.personal_information_score = personal_information_score
    
