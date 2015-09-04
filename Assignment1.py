#!/usr/bin/python
import Queue


#  1:  Queue module
class qMod():

  def __init__(self):
    self.Q = Queue.Queue();

  def add(self, val):
    self.Q.put(val);
    print "submit: ",val;


  def DQ(self):
    print "DQ: ",self.Q.get();



#  2: Stack using a list
class stack():


  def __init__(self):
    self.stk=[];

  def push(self, val):
    self.stk.append(val);
    print "pushed: ",val

  def pop(self):
    print "popped: ",self.stk.pop();

  def checkSize(self):
    print "size is: ",len(self.stk);



#  3:create a binary search tree
class node(object):

  def __init__(self,key=None,right=None,left=None,parent=None):
    self.key=key;
    self.right=right;
    self.left=left;
    self.parent=parent;

class bTree(object):

  def __init__(self,key):
    root_node=node(key,None,None,None);
    self.root=root_node;


  #  Find is being used in add
  def find(self, parentkey, node):
    self.ret=None;
    if node.key is parentkey:
      #print "parent found"
      self.ret=node;
    else:
      if node.left is not None:
        self.ret=self.find(parentkey,node.left);
        #right child exists and left child didnt find it
      if node.right is not None and self.ret is None:
        self.ret=self.find(parentkey,node.right);
    return self.ret;


  def add(self,key, parentkey):
    parent_node=self.find(parentkey,self.root);
    if parent_node is not None:
      if parent_node.left is not None and parent_node.right is not None:
        #print "parent has two children node not added";
        return None;
      elif parent_node.left is None:
        new_node=node(key,None,None,parent_node);
        parent_node.left=new_node;
        #print "added left node"
        #print new_node.key;
      elif parent_node.right is None:
        new_node=node(key,None,None,parent_node);
        parent_node.right=new_node;
        #print "added right node"
        #print new_node.key;
    else:
        print "parent node not found";



  def PreOrder(self,node):
    if node is None:
      return;
    else:
      print node.key;
      self.PreOrder(node.left);
      self.PreOrder(node.right);

#    if node is not None:
      #print node.key;
#     if node.left is not None:
#       print node.left.key;
#     if node.right is not None:
#       print node.right.key;
#     if node.left is not None:
#       self.PreOrder(node.left);
#     if node.right is not None:
#       self.PreOrder(node.right);


  def Print(self):
    print "PRINTING BST:\n"
    self.PreOrder(self.root);


  def delete(self,key):
    delete_node=self.find(key,self.root);
    if delete_node is not None:
      if delete_node.left is None and delete_node.right is None:
        #delete the node
        if delete_node.parent.left is delete_node:
          delete_node.parent.left=None;
          delete_node.parent=None;
        elif delete_node.parent.right is delete_node:
          delete_node.parent.right=None;
          delete_node.parent=None;
        else:
          print "delete node is not a child of its parent";
      else:
        print "Node not deleted, has children";
    else:
      print "Node not found";





# 4. Graph class
class vertex(object):
  def __init__(self,val):
    self.val=val;
    self.edges=[];



class graph():

  def __init__(self):
    self.vertex=[];

  def isValid(self,val):
    self.chk_valid=1;
    for i in self.vertex:
      if i is val:
        self.chk_valid=0;
    return self.chk_valid;

  def addVertex(self,val):
    self.valid=self.isValid(val);
    if self.valid is 1:
      #vertex does not already exist
      new_vertex=vertex(val);
      self.vertex.append(new_vertex);

    elif self.valid is 0:
      #vertex already exists
      print "vertex already exists";


  def addEdge(self,val1,val2):
    self.vertex1=self.retVertex(val1);
    self.vertex2=self.retVertex(val2);
    if self.vertex1 is not None and self.vertex2 is not None:
      self.vertex1.edges.append(val2);
      self.vertex2.edges.append(val1);
    else:
      print "one or more verticies not found";


  def retVertex(self,val):
    i=0;
    for i in range(len(self.vertex)):
      if self.vertex[i].val is val:
        return self.vertex[i];
    return None;


  def findVertex(self,val):
    self.find_vertex=None;
    self.find_vertex=self.retVertex(val);
    if self.find_vertex is None:
      print "vertex could not be found";
    else:
      print "found vertex";
      for i in self.find_vertex.edges:
        print "Edge", self.find_vertex.val,"-->",i



#  START OF TEST CODE


#  Testing the Queue
print "\n\n\n\nSTART OF QUEUE TEST:"
q=qMod();

for i in range(10):
  q.add(i);
for i in range(10):
  q.DQ();


#  Testing the stack
print "\n\n\n\nSTART OF STACK TEST:"
s=stack();
for i in range(10):
  s.push(i);

s.checkSize();

for i in range(10):
  s.pop();

s.checkSize();

#  Testing the BST
print "\n\n\n\nSTART OF BST TEST:"
b=bTree(0); #add root 
b.add(1,0); #root left child
b.add(2,0); #root right child
b.add(3,1); #root->left->left
b.add(4,1); #root->right->left
b.add(5,2);
b.add(6,2);
b.add(7,3);
b.add(8,3);
b.add(9,4);
b.add(10,4);
b.add(11,5);
b.add(12,5);
b.Print();
b.delete(10);
b.delete(12);
b.delete(8);
b.Print();

#  Testing the graph
print "\n\n\n\nSTART OF GRAPH TEST:"
g=graph();
for i in range(16):
  g.addVertex(i);

g.addEdge(0,3);
g.addEdge(2,1);
g.addEdge(2,4);
g.addEdge(2,5);
g.addEdge(2,6);
g.addEdge(3,4);
g.addEdge(3,5);
g.addEdge(15,1);
g.addEdge(15,2);
g.addEdge(15,3);
g.addEdge(14,6);
g.addEdge(14,7);
g.addEdge(14,8);
g.addEdge(13,15);
g.addEdge(13,14);
g.addEdge(13,0);
g.addEdge(12,0);
g.addEdge(9,0);
g.addEdge(15,0);
g.addEdge(10,11);
g.addEdge(13,12);
g.addEdge(13,2);

g.findVertex(3);
g.findVertex(15);
g.findVertex(0);
