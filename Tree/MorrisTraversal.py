class TreeNode:
        def __init__(self , val= 0 , left = None , right = None):
                self.val = val
                self.left = left
                self.right = right 

class Tree:
        def insert(self, root, data):
                if not root:
                        return TreeNode(data)
                if root.val >= data:
                        root.left = self.insert(root.left , data)
                        return root
                else:
                        root.right = self.insert(root.right , data)
                        return root

        def inorder(self, root):
                if not root:
                        return
                self.inorder(root.left)
                print(root.val)
                self.inorder(root.right)

        def preorder(self , root):
                if not root:
                        return

                print(root.val)
                self.preorder(root.left)
                self.preorder(root.right)

        def postorder(self , root):
                if not root:
                        return

                self.postorder(root.left)
                self.postorder(root.right)
                print(root.val)

        def morris_inorder(self , root):
                if not root :
                        return []

                inorder = list()

                while(root):
                        if not root.left:
                                inorder.append(root.val)
                                root = root.right
                        else:
                                curr = root.left

                                while(curr.right and curr.right != root):
                                        curr = curr.right

                                if not curr.right:
                                        curr.right = root
                                        root = root.left

                                elif curr.right == root:
                                        curr.right = None
                                        inorder.append(root.val)
                                        root = root.right

                return inorder

        def morris_preorder(self, root):
                if not root :
                        return list()

                preorder  = list()

                while(root):
                        if not root.left:
                                preorder.append(root.val)
                                root = root.right

                        else:
                                curr = root.left
                        
                                while(curr.right and curr.right != root):
                                        curr = curr.right

                                if not curr.right :
                                        curr.right = root
                                        preorder.append(root.val)
                                        root = root.left

                                elif curr.right == root:
                                        curr.right = None
                                        root = root.right
                                        
                return preorder

        def morris_postorder(self , root):
                if not root :
                        return list()
                        
                postorder = list()

                while(root):
                        if not root.right:
                                postorder.append(root.val)
                                root = root.left
                        else:
                                curr = root.right
                                        
                                while(curr.left and curr.left != root):
                                        curr = curr.left

                                if not curr.left:
                                        curr.left = root
                                        postorder.append(root.val)
                                        root = root.right
                                else:
                                        curr.left = None
                                        root = root.left

                postorder.reverse()
                return postorder

                                
if __name__ ==  "__main__":
        Tree1 = Tree()
        #root = TreeNode(10)
        root = Tree1.insert(None, 4)
        root = Tree1.insert(root, 5)
        root = Tree1.insert(root, 2)
        root = Tree1.insert(root, 7)
        root = Tree1.insert(root, 9)
        root = Tree1.insert(root, 1)

        #Tree1.inorder(root)
        #Tree1.preorder(root)
        Tree1.postorder(root)

        #inorder = Tree1.morris_inorder(root)
        #print("inorder : " , inorder)
        #preorder = Tree1.morris_preorder(root)
        #5print("preorder : " , preorder)
        postorder = Tree1.morris_postorder(root)
        print("postorder : " , postorder)

        
	
