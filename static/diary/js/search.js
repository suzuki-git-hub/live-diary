window.addEventListener("load",function(){

  const search = document.querySelector("#search");

  search.addEventListener("input",function(event){
  //↑入力欄に何か入力されたら発動。入力された内容を受け取るためにevent引数を設置。
    console.log(event.currentTarget.value);
  //↑event.currentTarget は、イベントが発生した要素を参照する。

    let words      = event.currentTarget.value;
    //↑入力された内容を抜き取って変数へ代入

  

    let words_list = words.replace(/　/g,' ').split(' ');
    //↑全角を半角にして半角区切りでリストにする

    let old_data  = data;
    //↑検索対象のdateを一旦old_dateに代入

    if (words_list.length === 0) {//words_listの長さが0（つまり、words_listが空である）と等しいかどうかを確認。そして、この条件式がtrueの場合、次のブロックが実行される。したがって、条件式がtrue（words_listが空）の場合、displayFolders(data)関数が実行され、その後に関数の実行が終了します。条件式がfalse（words_listが空でない）の場合、このブロックはスキップされ、条件式の次の行の処理が続行され
      displayFolders(data);
      return;
    }

    for(let w of words_list){ 
    //↑forループでリストにしたキーワードを回す
    //let を使用することで、変数のスコープを for ループのブロック内に制限する。変数の有効範囲がループ内に制限されるため、スコープの衝突や意図しない動作を防ぐ。
      let new_data = [];
    //↑キーワードのループのたびに新しい配列を作りなおす
        for(let d of old_data){ //検索対象をforループしてキーワードと一致したら新たな変数に代入
          if("search" in d){
            if(d["search"].toLowerCase().indexOf(w.toLowerCase())!==-1){
              new_data.push(d); 
               //.toLowerCaseとは文字列型に実行できるメソッド。小文字にしてくれる。
               //.indexOfとは引数に入れた文字列を含んでいれば、その文字列の位置を返し、含んでなければ−１を返す。今回の場合は−１ではない場合push。
            }
          }
          else{
            if(d["title"].toLowerCase().indexOf(w.toLowerCase())!==-1)
              new_data.push(d);
          }
          
        }
        old_data = new_data;
        //キーワードにと一致したオブジェクトだけのnew_dataを代入して上書きする
    }
    displayFolders(old_data);//displayFoldersという関数を呼び出す。displayFoldersという関数がold_dataという引数を受け取って実行される。
 });

 
  function displayFolders(data) {
    let result = "";
    for (let w of data) {
      if ("search" in w){
          result += '<a href="' + w['link'] + '" class="diary_item"><img src="' + w["thumbnail"] + '" >' + w["title"] + '</a> '; 
      }
      else{
        result += '<a href="' + w['link'] + '" class="diary_item">' + w["title"] + '</a> ';
      }
   //w['link']は、wというオブジェクトから'link'というキーに対応する値を取得し、同様にw["title"]はwから"title"というキーに対応する値を取得している。  
    }
    let result_elem = document.querySelector("#search_result");
      result_elem.innerHTML = result;
  }
  

  displayFolders(data);




});