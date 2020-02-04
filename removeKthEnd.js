const Node = require('./node');

function removeKth(head,k) {
  //move to end of LL
  let node = head;
  let count = 0;
  linkedlist = [];

  while (node) {
    node = node.next;
    linkedlist.push(node);
    count++;
  }
//   console.log(count,node);
  const listIndex = count - (k+1);
  const prev = linkedlist[listIndex-1];
  const current = linkedlist[listIndex];
  prev.next = current.next;
  return head;
}

n = new Node(1);
head = n;

for (let i=2; i<=20; i++) {
  n.next = new Node(i);
  n = n.next;
}

const h = removeKth(head,15)
let node = h;
const vals = []
while (node) {
  vals.push(node.data)
  node = node.next;
}
console.log(vals);







