import java.util.Scanner;
///Creating a Node for creating objects 
class Node {
    int data;
    Node next;
    Node(int data){
        this.data = data;
        this.next = next;
    }
}


class LinkedList{
    Node head,tail;
    //contructor 
    LinkedList(){
        this.head = null;
        this.tail = null;
    }
    // checking whether the LinkedList is Empty or not 
    boolean isEmpty(){
        return head == null;
    }
    // inserting the position from the user 
    int insertPosition(){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the position: ");
        int pos = sc.nextInt();
        return pos;
    }
    
    // Creating a New Node with the specified element 
    Node createNode(){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the data: ");
        int data = sc.nextInt();
        Node newNode = new Node(data);
        return newNode;
    }
    // adding a new Node at the first 
    void addFirst(){
        Node newNode = createNode();
        if(isEmpty()) {
            head = tail = newNode;
        }else {
            newNode.next = head;
            head = newNode;
        }
    }
    // adding a new Node at the Last 
    void addMiddle(){
        if(isEmpty()){
            addFirst();
            return;
        }else {
            int pos = insertPosition();
            if(pos == 0){
                addFirst();
                return;
            }
            Node newNode = createNode();
            Node temp = head;
            for(int i = 0;i < pos-1;i++){
                temp = temp.next;
            }newNode.next = temp.next;
            temp.next = newNode;
        }
    }
    
    // adding a newNode at the last 
    void addLast(){
        if(isEmpty()){
            addFirst();
            return;
        }else{
            Node newNode = createNode();
            tail.next = newNode;
        }
    }
    
    // displaying the Linked List 
    void display(){
        if(isEmpty()){
            System.out.println("Linked List is Empty!!.");
        }else {
            Node temp = head;
            while(temp != null){
                System.out.print(temp.data + " ");
                temp = temp.next;
            }System.out.println();
        }
    }
    
}


class Main{
    public static void main(String args[]){
        LinkedList list = new LinkedList();
        list.addFirst();
        list.addFirst();
        list.addFirst();
        list.display();
        list.addMiddle();
        list.display();
        list.addLast();
        list.display();
    }
}