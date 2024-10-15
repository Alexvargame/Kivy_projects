from models import  User, Phone

def phone_saver(name, phones):
    if name and phones:
        user = User.add(name)
        for phone in phones.split("\n"):
            Phone.add(phone, user)
        return True
    return False

def show_all_for_name(name):
    return [tuple([user.name, ', '.join([p.phone for p in user.phones]), user.id]) for user in User.find_by_name(name)]

def show_all_for_phone(phone):
    return [tuple([user.name, ', '.join([p.phone for p in user.phones]), user.id]) for user in User.find_by_phone(phone)]

def show_all_phones():
    return [tuple([user.name, ', '.join([p.phone for p in user.phones]), user.id]) for user in User.all()]

def delete_by_id(user_id):
    return User.delete_by_id(user_id)

# def phone_search_and_populate_results_list(self, query):
#     print(query)
#
#
# def save_contact_and_switch_to_search(self, name, phones):
#     print(name, phones)