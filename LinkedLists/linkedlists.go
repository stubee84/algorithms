package main

import "fmt"

type doublyLinkedList struct {
	head, tail bool
	prev       *doublyLinkedList
	next       *doublyLinkedList
	text       string
	length     int
}

func (l *doublyLinkedList) New(first, last bool, p, n *doublyLinkedList, t string, count int) {
	l.head = first
	l.tail = last
	l.prev = p
	l.next = n
	l.text = t
	l.length = count
}

func (l *doublyLinkedList) addToEnd(t string) {
	head := l

	for {
		//last item in the list
		if l.head == false && l.tail == true {
			d := doublyLinkedList{}
			d.New(false, true, nil, nil, t, l.length+1)

			//set current node tail bool value to false, it is no longer the tail
			l.tail = false

			//point previous to itself, set head.prev to the pointer of tail, set next to the pointer of the tail
			l.prev = l
			head.prev = &d
			d.next = head
			l.next = &d
			return
		} else if l.head == true && l.tail == true {
			d := doublyLinkedList{}
			d.New(false, true, nil, nil, t, l.length+1)

			l.tail = false

			//set the previous to the tail, the next to the tail, and set the next for the tail to the head
			l.prev = &d
			d.next = l
			l.next = &d
			return
		}
		l = l.next
	}
}

//when you find the tail in the next node set the current next to the head (since it is now the tail) and se the prev in head to the tail
func (l *doublyLinkedList) delFromEnd() {
	head := l
	for {
		if l.next.tail == true && l.next.head == false {
			l.tail = true
			l.next = head
			head.prev = l
			return
		}
		l = l.next
	}
}

func (l *doublyLinkedList) printAll() {
	for {
		fmt.Println(l.text, l.length)
		if l.tail == true {
			return
		}
		l = l.next
	}
}

//return the length of the tail
func (l *doublyLinkedList) getLength() int {
	return l.prev.length
}

//find the index at list length and return the pointer to the doubleyLinkedList
func (l *doublyLinkedList) getAtIndex(index int) *doublyLinkedList {
	for {
		if l.length == index {
			return l
		}
		l = l.next
	}
}

func (l *doublyLinkedList) insertAt(index int, t string) {
	//grab the length of the list to iterate through
	count := l.prev.length
	for i := 0; i <= count; i++ {
		if l.length == index {
			d := doublyLinkedList{}
			d.New(false, false, nil, nil, t, index)

			//if this is the beginning node then set the new node as head
			if l.head == true {
				l.head = false
				d.head = true
			}

			//re-assign pointers
			d.prev = l.prev
			d.next = l.next
			l.prev.next = &d
			l.next.prev = &d

			//traverse to next node
			l = l.next
		}
		if l.length >= index {
			//increment length only if we have inserted the new node
			l.length++
		}
		l = l.next
	}
}

func main() {

	list := doublyLinkedList{}

	//the first item is both the head and tail
	list.New(true, true, nil, nil, "page1", 0)
	list.addToEnd("page2")
	list.addToEnd("page3")
	list.addToEnd("page4")
	list.addToEnd("page5")
	list.insertAt(3, "insertion")

	list.printAll()

	list.delFromEnd()

	list.printAll()
	fmt.Println(list.getLength())
	fmt.Println(list.getAtIndex(2).text)
}
