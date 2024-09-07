#include <iostream>
#include <string>
#include <vector>

struct person {
    std::string name;
    int age;
};

person combine(std::string name, int age) {
    person p;
    p.name = name;
    p.age = age;
    return p;
}

std::vector<person> combineList(std::vector<std::string> names, std::vector<int> ages) {
    std::vector<person> people;
    for (int i = 0; i < names.size(); i++) {
        people.push_back(combine(names[i], ages[i]));
    }
    return people;
}

void sort_by_age(std::vector<person>& people, bool ascending = true) {
    if (ascending) {
        for (int i = 0; i < people.size(); i++) {
            for (int j = i + 1; j < people.size(); j++) {
                if (people[i].age > people[j].age) {
                    person temp = people[i];
                    people[i] = people[j];
                    people[j] = temp;
                }
            }
        }
    } else {
        for (int i = 0; i < people.size(); i++) {
            for (int j = i + 1; j < people.size(); j++) {
                if (people[i].age < people[j].age) {
                    person temp = people[i];
                    people[i] = people[j];
                    people[j] = temp;
                }
            }
        }
    }
}

std::vector<std::string> extract_names(std::vector<person> people) {
    std::vector<std::string> names;
    for (int i = 0; i < people.size(); i++) {
        names.push_back(people[i].name);
    }
    return names;
}

std::vector<int> extract_ages(std::vector<person> people) {
    std::vector<int> ages;
    for (int i = 0; i < people.size(); i++) {
        ages.push_back(people[i].age);
    }
    return ages;
}

//////////////////////////////////////////////////////////////////////////////////////////

template <class T>
int sizeOfList(T arr){
    int size = 0;
    while (arr[size] != nullptr){
        size++;
    }
    return size;
}

person* combineList2 (char* nameList[], int* ageList, int size){
    person* peopleList = new person[size];
    for (int i = 0; i < size; i++){
        peopleList[i].name = nameList[i];
        peopleList[i].age = ageList[i];
    }
    return peopleList;
}

char** extract_names2(person* peopleList, int size){
    char** names = new char*[size + 1];
    for (int i = 0; i < size; i++) {
        names[i] = new char[peopleList[i].name.size() + 1];
        for(int j = 0; j < peopleList[i].name.size(); j++){
            names[i][j] = peopleList[i].name[j];
        }
        names[i][peopleList[i].name.size()] = '\0';
    }
    names[size] = nullptr;
    return names;
}

int* extract_ages2(person* peopleList, int size){
    int* ages = new int[size];
    for (int i = 0; i < size; i++){
        ages[i] = peopleList[i].age;
    }
    return ages;
}


int main(){
    std::vector<std::string> nameList = {"John", "Mary", "Bob", "Alice", "Tom"};
    std::vector<int> ageList = {31, 12, 25, 13, 21};

    std::vector<person> people = combineList(nameList, ageList);
    sort_by_age(people, false);
    std::vector<std::string> names = extract_names(people);
    std::vector<int> ages = extract_ages(people);

    std::cout << "PersonList1 : " << std::endl;
    for (int i = 0; i < names.size(); i++) {
        std::cout << names[i] << " " << ages[i] << std::endl;
    }
    std::cout << std::endl;

    char* name_list2[] = {"Mike", "Waltuh", "Saul", "Jimmy", "Pink", nullptr};


    int* age_list2 = new int[5];
    age_list2[0] = 17;
    age_list2[1] = 12;
    age_list2[2] = 4;
    age_list2[3] = 15;
    age_list2[4] = 33;
    

    int size = sizeOfList(name_list2);
    person* people2 = combineList2(name_list2, age_list2, size);
    char** names2 = extract_names2(people2, size);
    int* ages2 = extract_ages2(people2, size);

    std::cout << "PersonList2 : " << std::endl;
    for (int i = 0; i < size; i++) {
        std::cout << names2[i] << " " << ages2[i] << std::endl;
    }
    std::cout << std::endl;
    
    return 0;
}