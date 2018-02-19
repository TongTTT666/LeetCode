# 法1：深度优先搜索
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        # 很显然的深度优先搜索救恩能够搞定的问题，递归调用
        r, c = len(image), len(image[0])
        originColor = image[sr][sc]
        # 有一种比较变态的情况，就是更改后的颜色与更改前的颜色一样
        # 那就不更改啊。。。
        if originColor == newColor:
            return image
        
        def DFS(image, sr, sc, newColor):
            # 先标记搜索过的节点，在这里直接就标记为新颜色
            image[sr][sc] = newColor
            if sr + 1 < r and originColor == image[sr+1][sc]:
                DFS(image, sr+1, sc, newColor)
            if sc + 1 < c and originColor == image[sr][sc+1]:
                DFS(image, sr, sc+1, newColor)
            if sr - 1 >= 0 and originColor == image[sr-1][sc]:
                DFS(image, sr-1, sc, newColor)
            if sc - 1 >= 0 and originColor == image[sr][sc-1]:
                DFS(image, sr, sc-1, newColor)
                
        DFS(image, sr, sc, newColor)
        return image



# 法2：宽度优先搜索

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        # 很显然的深度优先搜索救恩能够搞定的问题，递归调用
        r, c = len(image), len(image[0])
        originColor = image[sr][sc]
        # 有一种比较变态的情况，就是更改后的颜色与更改前的颜色一样
        # 那就不更改啊。。。
        if originColor == newColor:
            return image
        # 继续尝试宽度优先搜索，需要一个队列
        queue = []
        # 原始出发点也要做标记哦！
        image[sr][sc] = newColor
        queue.append((sr, sc))
        # 只要队列里面有值
        while queue:
            coo = queue.pop(0)
            if coo[0] + 1 < r and originColor == image[coo[0]+1][coo[1]]:
                # 做标记 说明该点被访问过了
                image[coo[0]+1][coo[1]] = newColor
                # 推入队列 这个点还有价值，因为会延伸出旁边的点
                queue.append((coo[0]+1, coo[1]))
            if coo[1] + 1 < c and originColor == image[coo[0]][coo[1]+1]:
                # 做标记 说明该点被访问过了
                image[coo[0]][coo[1]+1] = newColor
                # 推入队列 这个点还有价值，因为会延伸出旁边的点
                queue.append((coo[0], coo[1]+1))
            if coo[0] - 1 >= 0 and originColor == image[coo[0]-1][coo[1]]:
                # 做标记 说明该点被访问过了
                image[coo[0]-1][coo[1]] = newColor
                # 推入队列 这个点还有价值，因为会延伸出旁边的点
                queue.append((coo[0]-1, coo[1]))
            if coo[1] - 1 >= 0 and originColor == image[coo[0]][coo[1]-1]:
                # 做标记 说明该点被访问过了
                image[coo[0]][coo[1]-1] = newColor
                # 推入队列 这个点还有价值，因为会延伸出旁边的点
                queue.append((coo[0], coo[1]-1))
                
        return image
