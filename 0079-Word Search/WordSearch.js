/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    if(board.length == 0 || board[0].length == 0) return false;
    var visited = [];
    for(var i = 0;i<board.length;i++){
        var a = [];
        for(var j=0;j<board[0].length;j++){
            a.push(0);
        }
        visited.push(a);
    }

    for(i = 0;i<board.length;i++){
        for(j=0;j<board[0].length;j++){
            if(search(board, word, [i,j], 0, 0, visited))
                return true;
        }
    }
    return false;
};

function search(board, word, boardIndex, wordIndex, count, visited){
    if(word.length == wordIndex)
        return true;

    var i = boardIndex[0];
    var j = boardIndex[1];
    if(i<0 || j<0 || i>=board.length || j>=board[0].length || visited[i][j] || board[i][j] != word[wordIndex]){
        return false;
    }
    // console.log(board[boardIndex[0]][boardIndex[1]] + "("+boardIndex + ")wordIndex: " +wordIndex);

    // if(board[i][j] == word[wordIndex]){
    //     board[i][j]=' ';
    //     wordIndex++;
    //     count++;
    // }
    visited[i][j] = 1;
    // console.log(visited);
    if(search(board, word, [i+1, j], wordIndex+1, count, visited)) return true;
    if(search(board, word, [i, j+1], wordIndex+1, count, visited)) return true;
    if(search(board, word, [i-1, j], wordIndex+1, count, visited)) return true;
    if(search(board, word, [i, j-1], wordIndex+1, count, visited)) return true;
    visited[i][j] = 0;
    return false;
}
var board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
];

var word = "ABCCED";
// for(var i = 0;i<3;i++){
//     var a = [];
//     for(var j=0;j<4;j++){
//         console.log(board[i][j]);
//     }
// }
console.log(exist(board, word));
