class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        start_color = image[sr][sc]   
        #если цвет уже такой же, то ничего делать не нужно
        if start_color == color:
            return image   
        def dfs(r, c):
            #проверка выхода за границы
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return       
            #если цвет не совпадает, то пропускает
            if image[r][c] != start_color:
                return          
            #перекрашивает текущую клетку
            image[r][c] = color          
            #идёт в 4 направления
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)     
        #запускает обход
        dfs(sr, sc)       
        return image       