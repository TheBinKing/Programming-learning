#include "queue"
#include "stack"
#include "vector"
#include <iostream>
using namespace std;

class BiNode {
public:
	char data;
	struct BiNode* lnode, * rnode;
};
class BiTree {
private:
    BiNode* root;
    int height;
    void pre_Order(BiNode* t);
    void in_Order(BiNode* t);
    void post_Order(BiNode* t);
    BiNode* Create(string& s, int& pos);
    void get_Height(BiNode* t, int h);
public:
    BiTree() { root = NULL;height = 0; }
    ///按照前序遍历序列创建二叉树
    void createBiTree(string s);
    ///前序遍历二叉树
    void preOrder();
    ///中序遍历二叉树
    void inOrder();
    ///后序遍历二叉树(递归方法)
    void postOrder();
    ///后序遍历二叉树(使用栈的非递归方法)
    void postOrder1();
    ///层序遍历二叉树
    void levelOrder();
    ///求树的高度
    int getHeight();
    ///求两个节点的最大公共祖先
    void ancestor(char A, char B);
};
BiNode* BiTree::Create(string& s, int& pos) {
	++pos;
	BiNode* t;
	if (pos >= s.size())
		return NULL;
	else
	{
		if (s[pos] == '#')
			t = NULL;
		else
		{
			t = new BiNode;
			t->data = s[pos];
			t->lnode = Create(s, pos);
			t->rnode = Create(s, pos);
		}
		return t;
	}
}

void BiTree::createBiTree(string s) {

	int pos = -1;
	root = Create(s, pos);

}

//pre
void BiTree::preOrder() {
    pre_Order(root);
    cout << endl;
}
void BiTree::pre_Order(BiNode* t) {
    if (t != NULL) {
        cout << t->data << ' ';
        pre_Order(t->lnode);
        pre_Order(t->rnode);
    }
}

//in
void BiTree::inOrder() {
    in_Order(root);
    cout << endl;
}
void BiTree::in_Order(BiNode* t) {
    if (t != NULL) {
        in_Order(t->lnode);
        cout << t->data << ' ';
        in_Order(t->rnode);
    }
}

//back
void BiTree::postOrder() {
    post_Order(root);
    cout << endl;
}
void BiTree::post_Order(BiNode* t) {
    if (t != NULL) {
        post_Order(t->lnode);
        post_Order(t->rnode);
        cout << t -> data << ' ';

    }
}

void BiTree::postOrder1() {
    BiNode* p, * r;
    r = NULL;
    p = root;
    stack<BiNode*> my_stack;
    while (p!=NULL||!my_stack.empty())
    {
        if (p) {
            my_stack.push(p);
            p = p->lnode;
        }
        else
        {
            p = my_stack.top(); //栈内容不会被改变
            if (p->rnode != NULL && p->rnode != r) {
                p = p->rnode;
                my_stack.push(p);
                p = p->lnode;
            }
            else
            {
                p = my_stack.top();
                my_stack.pop();
                cout << p->data << ' ';
                r = p;
                p = NULL;
            }
        }
    }
    cout << endl;

}

void BiTree::levelOrder() {
    if (root == NULL)
        return;
    queue<BiNode*>q;
    q.push(root);
    while (!q.empty()) {
        BiNode* t;
        t = q.front();
        q.pop();
        cout << t->data << ' ';
        if (t->lnode != NULL)
            q.push(t->lnode);
        if (t->rnode != NULL)
            q.push(t->rnode);
    }
    cout << endl;
}

int BiTree::getHeight() {
    get_Height(root, 0);
    return height;
}
void BiTree::get_Height(BiNode* t, int h) {
    if (t != NULL) {
        ++h;
        if (h > height)
            height=h;
        get_Height(t->lnode, h);
        get_Height(t->rnode, h);
    }
}


int main() {
    BiTree a;
    string s;
    s = "ABD##E#F##C##";
    a.createBiTree(s);
    cout << "前序遍历" << endl;
    a.preOrder();

    cout << "中序遍历" << endl;
    a.inOrder();

    cout << "后序遍历1" << endl;
    a.postOrder();

    cout << "后续遍历2" << endl;
    a.postOrder1();

    cout << "层次遍历" << endl;
    a.levelOrder();
    
    cout << "树高:" << endl;
    cout << a.getHeight() << endl;

    return 0;
}
