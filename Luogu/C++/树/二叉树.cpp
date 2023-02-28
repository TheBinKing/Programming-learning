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
    ///����ǰ��������д���������
    void createBiTree(string s);
    ///ǰ�����������
    void preOrder();
    ///�������������
    void inOrder();
    ///�������������(�ݹ鷽��)
    void postOrder();
    ///�������������(ʹ��ջ�ķǵݹ鷽��)
    void postOrder1();
    ///�������������
    void levelOrder();
    ///�����ĸ߶�
    int getHeight();
    ///�������ڵ����󹫹�����
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
            p = my_stack.top(); //ջ���ݲ��ᱻ�ı�
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
    cout << "ǰ�����" << endl;
    a.preOrder();

    cout << "�������" << endl;
    a.inOrder();

    cout << "�������1" << endl;
    a.postOrder();

    cout << "��������2" << endl;
    a.postOrder1();

    cout << "��α���" << endl;
    a.levelOrder();
    
    cout << "����:" << endl;
    cout << a.getHeight() << endl;

    return 0;
}
