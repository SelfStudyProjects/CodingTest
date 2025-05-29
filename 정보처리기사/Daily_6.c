#include <stdio.h>

#include <stdlib.h>

​

typedef struct _node {

  int data;

  struct _node *next;

} node;

node *head, *tail;

void init_list(void){

  head = (node *)malloc(sizeof(node));

  tail = (node *)malloc(sizeof(node));

  head->next = tail;

  tail->next = NULL;

}

node *insert(int k){

  node *p = head;

  node *new_node = (node *)malloc(sizeof(node));

  new_node->data = k;

  while(p->next != tail && p->next->data < k) {

    p = p->next;

  }

  new_node->next = p->next;

  p->next = new_node;

  return new_node;

}

​

void print_list(node *t){

  while(t != tail) {

    printf("%d", t->data);

    t = t->next;

  }

}

int delete_node(int k){

  node *p = head;

  node *temp;

  while(p->next != tail  

      && p->next->data != k) {

    p = p->next;

  }

  if(p->next == tail) {

    return -1; 

  }

  temp = p->next;

  p->next = temp->next;

  free(temp);

  return 0; 

}

​

int main(){

  init_list();

  insert(10);

  insert(5);

  insert(8);

  insert(3);

  delete_node(8);

  print_list(head->next);

  return 0;

}