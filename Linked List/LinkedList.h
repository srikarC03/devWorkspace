#include <iostream>
#include <vector>
using namespace std;

template <typename T>
class LinkedList{
    public:
        class Node{
            public:
            T val;
            Node* next;
            Node* prev;
        };
        // Constructor and Destructor
        LinkedList(){
            count = 0;
            head = nullptr;
            tail = nullptr;
        }
        LinkedList(const LinkedList<T>& list);
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
        const T& operator[](unsigned int index) const;
        T& operator[](unsigned int index);
        bool operator==(const LinkedList<T>& rhs);
        LinkedList<T>& operator=(const LinkedList<T>& rhs);

        // Accessors
        unsigned int NodeCount() const{
            return count;
        }
        void FindAll(vector<Node*>& outData, const T& value) const;
        const Node* Find(const T& data) const;
        const Node* GetNode(unsigned int index) const;
        Node* GetNode(unsigned int index);
        Node* Head();
        const Node* Head() const;
        Node* Tail();
        const Node* Tail() const;

        // Insertion

        void AddHead(const T& data){
            Node* newNode = new Node();
            newNode->val = data;
            newNode->next = nullptr;
            newNode->prev = nullptr;
            if(head==nullptr){
                head = newNode;
                tail = newNode;
                head->next = nullptr;
                head->prev = nullptr;
            }
            else{
                head->prev = newNode;
                if(count==1){
                    tail->prev = newNode;
                }
                newNode->next = head;
                head = newNode;
            }
            count+=1;
        }

        void AddTail(const T& data){
            Node* newNode = new Node();
            newNode->val = data;
            newNode->next = nullptr;
            newNode->prev = nullptr;

            if(tail == nullptr){
                head = newNode;
                tail = newNode;
                tail->next = nullptr;
                tail->prev = nullptr;
            }
            else{
                tail->next = newNode;
                if(count==1){
                    head->next = newNode;
                }
                newNode->prev = tail;
                newNode->next = nullptr;
                tail = newNode;
                newNode = nullptr;
            }
            count+=1;
            
        }
        void AddNodesHead(const T* data, unsigned int count){
            for(int i=(int)count-1; i>=0; i--){
                AddHead(data[i]);
            }
        }
        void AddNodesTail(const T* data, unsigned int count){
            for(unsigned int j = 0; j < count; j++){
                AddTail(data[j]);
            }
        }
        void InsertAfter(Node* node, const T& data);
        void InsertBefore(Node* node, const T& data);
        void InsertAt(const T& data, unsigned int index);

        // Removal
        bool RemoveHead();
        bool RemoveTail();
        unsigned int Remove(const T& data);
        bool RemoveAt(unsigned int index);
        void Clear();


        // Behaviors
        void PrintForward() const{
            Node* currPtr = head;
            while(currPtr!=nullptr){
                cout << currPtr->val << endl;
                currPtr = currPtr->next;
            }
        }
        void PrintReverse() const{
            Node* currPtr = tail;
            while(currPtr!=nullptr){
                cout << currPtr->val << endl;
                currPtr = currPtr->prev;
            }
        }
        void PrintForwardRecursive(const Node* node) const;
        void PrintReverseRecursive(const Node* node) const;

    private:
        unsigned int count;
        Node* head;
        Node* tail;
};

