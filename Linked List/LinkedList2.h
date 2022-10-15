#include <iostream>
#include <vector>
using namespace std;

template <typename T>
class LinkedList{
    public:
        class Node{
            public:
            T data;
            Node* next;
            Node* prev;
        };
        // Constructor and Destructor
        LinkedList(){
            count = 0;
            head = nullptr;
            tail = nullptr;
        }
        LinkedList(const LinkedList<T>& list){
            count = 0;
            head = nullptr;
            tail = nullptr;
            unsigned int copyCount = list.NodeCount();
            for(unsigned int k=0; k<copyCount; k++){
                AddTail(list.GetNode(k)->data);
            }
        }
        ~LinkedList(){
            Node* nextPtr;
            Node* currPtr = head;
            while(currPtr!=nullptr){
                nextPtr = currPtr->next;
                delete currPtr;
                currPtr = nextPtr;
            }
            head = nullptr;
            tail = nullptr;
            count = 0;
        }

        // Operators
        const T& operator[](unsigned int index) const{

            if(index+1>count){
                throw out_of_range("Index out of Range");
            }
            else{
                unsigned int counter;
                Node* currPtr = head;
                for(counter = 0; counter<index; counter++){
                    currPtr = currPtr->next;
                }
                return currPtr->data;
            }
        }
        T& operator[](unsigned int index){
            
            if(index+1>count){
                throw out_of_range("Index out of Range");
            }
            else{
                unsigned int counter;
                Node* currPtr = head;
                for(counter = 0; counter<index; counter++){
                    currPtr = currPtr->next;
                }
                return currPtr->data;
            }
        }
        bool operator==(const LinkedList<T>& rhs){
            unsigned int counter = 0;
            if(count == 0 || rhs.count == 0){
                return true;
            }
            else if(count != rhs.count){
                return false;
            }
            else{
                while(GetNode(counter)->next != nullptr && rhs.GetNode(counter)->next != nullptr){
                    if(GetNode(counter)->data != rhs.GetNode(counter)->data){
                        return false;
                    }
                    else{
                        counter++;
                    }
                }
                return true;
            }
        }

        LinkedList<T>& operator=(const LinkedList<T>& rhs){
            unsigned int iter = count;
            for(unsigned int j=0; j<iter; j++){
                RemoveTail();
            }
            int copyCount = rhs.NodeCount();
            for(unsigned int a=0; a<copyCount; a++){
                AddTail(rhs.GetNode(a)->data);
            }
            return *this;
        }

        // Accessors
        unsigned int NodeCount() const{
            return count;
        }
        void FindAll(vector<Node*>& outData, const T& value) const{
            Node* currPtr = head;
            for(unsigned int j = 0; j<count; j++){
                if(currPtr->data == value){
                    outData.push_back(currPtr);
                }
                currPtr = currPtr->next;
            }
        }
        const Node* Find(const T& data) const{
            Node* currPtr = head;
            for(unsigned int i=0; i<count; i++){
                if(currPtr->data == data){
                    return currPtr;
                }
                currPtr = currPtr->next;
            }
            return nullptr;
        }
        Node* Find(const T& data){
            Node* currPtr = head;
            for(unsigned int i=0; i<count; i++){
                if(currPtr->data == data){
                    return currPtr;
                }
                currPtr = currPtr->next;
            }
            return nullptr;

        }
        const Node* GetNode(unsigned int index) const{
            if(index>count-1){
                throw out_of_range("GetNode1():Index out of Range");
            }
            else{
                Node* currPtr = head;
                for(unsigned int i = 0; i<index; i++){
                    currPtr = currPtr->next;
                }
                return currPtr;
            }
        }
        Node* GetNode(unsigned int index){
            
            if(index>count-1){
                throw out_of_range("GetNode2():Index out of Range");
            }
            else{
                Node* currPtr = head;
                for(unsigned int i = 0; i<index; i++){
                    currPtr = currPtr->next;
                }
                return currPtr;
            }
        }
        Node* Head(){
            return head;
        }
        const Node* Head() const{
            return head;
        }
        Node* Tail(){
            return tail;
        }
        const Node* Tail() const{
            return tail;
        }

        // Insertion

        void AddHead(const T& data){
            Node* newNode = new Node();
            newNode->data = data;
            newNode->next = nullptr;
            newNode->prev = nullptr;
            if(head==nullptr){
                head = newNode;
                tail = newNode;
                
            }
            else{
                head->prev = newNode;
                
                newNode->next = head;
                head = newNode;
            }
            newNode = nullptr;
            count+=1;
        }

        void AddTail(const T& data){
            Node* newNode = new Node();
            newNode->data = data;
            newNode->next = nullptr;
            newNode->prev = nullptr;

            if(tail == nullptr){
                head = newNode;
                tail = newNode;
                
            }
            else{
                tail->next = newNode;
                
                newNode->prev = tail;
                
                tail = newNode;
            }
            newNode = nullptr;
            count+=1;
            
        }
        void AddNodesHead(const T* data, unsigned int count){
           int inv = (int)count -1;
            for(int i= inv; i>=0; i--){
                AddHead(data[i]);
            }
        }
        void AddNodesTail(const T* data, unsigned int count){
            for(unsigned int j = 0; j < count; j++){
                AddTail(data[j]);
            }
        }
        void InsertAfter(Node* node, const T& data){
            Node* newNode = new Node();
            newNode->data = data;
            if(node->next == nullptr){
                node->next = newNode;
                newNode->prev = node;
                newNode->next = nullptr;
                tail = newNode;
            }
            else{
                Node* tmpNode = node->next;
                node->next = newNode;
                newNode->prev = node;
                newNode->next = tmpNode;
                tmpNode->prev = newNode;
            }
            count++;
        }
        void InsertBefore(Node* node, const T& data){
            Node* newNode = new Node();
            newNode->data = data;
            if(node->prev == nullptr){
                node->prev = newNode;
                newNode->next = node;
                newNode->prev = nullptr;
                head = newNode;
            }
            else{
                Node* tmpNode = node->prev;
                node->prev = newNode;
                newNode->next = node;
                newNode->prev = tmpNode;
                tmpNode->next = newNode;
            }
            count++;
        }
        void InsertAt(const T& data, unsigned int index){
            //cout << "InsertAt(): index = " << index << " count = " << count << endl;
            if(index>count){
                throw out_of_range("InsertAt():Index out of Range");
            }
            else if(index == count){
                InsertAfter(GetNode(index-1),data);
            }
            else{
                InsertBefore(GetNode(index),data);
            }
        }
        // Removal
        bool RemoveHead(){
            if(count==0){
                return false;
            }
            else{
                if(head->next == nullptr){
                    tail = nullptr;
                    delete head;
                    head = nullptr;
                }
                else{
                    Node* tmpPtr = head->next;
                    tmpPtr->prev = nullptr;
                    delete head;
                    head = tmpPtr;
                }
                count-=1;
                return true;
            }
        }
        bool RemoveTail(){
            if(count==0){
                return false;
            }
            else{
                if(tail->prev == nullptr){
                    head = nullptr;
                    delete tail;
                    tail = nullptr;

                }
                else{
                    Node* tmpPtr = tail->prev;
                    tmpPtr->next = nullptr;
                    delete tail;
                    tail = tmpPtr;
                }
                count-=1;
                return true;
            }
        }
        unsigned int Remove(const T& data){
            unsigned int copyCount = count;
            unsigned int numMatch = 0;
            for(unsigned int i = 0; i<copyCount; i++){
                if(GetNode(i-numMatch)->data == data){
                    RemoveAt(i-numMatch);
                    numMatch+=1;
                }
            }
            return numMatch;
        }
        bool RemoveAt(unsigned int index){
            //cout << "Index: " << index << " Count: " << count << endl;
            if(index<0 || index>count-1){
                return false;
            }
            else if(index == 0){
                return RemoveHead();
            }
            else if(index == count-1){
                return RemoveTail();
            }
            else{
                Node* currPtr = GetNode(index);
                Node* prevPtr = currPtr->prev;
                Node* nextPtr = currPtr->next;
                prevPtr->next = nextPtr;
                nextPtr->prev = prevPtr;
                delete currPtr;
                count-=1;
                return true;
            }
        }
        void Clear(){
            unsigned int copyCount = count;
            for(unsigned int i=0; i<copyCount; i++){
                RemoveTail();
            }
        }


        // Behaviors
        void PrintForward() const{
            Node* currPtr = head;
            while(currPtr!=nullptr){
                cout << currPtr->data << endl;
                currPtr = currPtr->next;
            }
        }
        void PrintReverse() const{
            Node* currPtr = tail;
            while(currPtr!=nullptr){
                cout << currPtr->data << endl;
                currPtr = currPtr->prev;
            }
        }
        void PrintForwardRecursive(const Node* node) const{
            if(node->next == nullptr){
                cout << node->data << endl;
                return;
            }

            cout << node->data << endl;

            return PrintForwardRecursive(node->next);
        }
        void PrintReverseRecursive(const Node* node) const{
            if(node->prev == nullptr){
                cout<< node->data << endl;
                return;
            }
            cout << node->data << endl;

            return PrintReverseRecursive(node->prev);
        }

    private:
        unsigned int count;
        Node* head;
        Node* tail;
};

