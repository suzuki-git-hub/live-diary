//jquery使用（長くなってしまうため）
window.addEventListener("load", function () {

  $("#add_artist").on("click", function () { add_artist() });
  //#add_artistがクリックされたときに、add_artist()という関数が実行される。
  $(document).on("click", ".add_song_btn", function () {
    add_song_btn(this)
  });
  // ページ全体がクリックされたとき、その時の要素が.add_setlistであればadd_setlistを実行
  // JavaScriptによって動的に追加された要素にイベントをセットするには、↑の書き方でないと発動しない


    // .fa-xmark アイコンがクリックされたときの処理
  $(document).on("click", ".fa-xmark", function () {
    // ここのthisは.fa-xmark アイコンを指す
    var parent = $(this).closest(".artist_area, .song_area");
    parent.remove();
    // .closest() メソッドは、jQuery ライブラリを使用して要素の階層構造をたどり、指定されたセレクタに最も近い親要素を検索する。
    // .fa-xmark アイコンの一番近い親要素で、.artist_area または .song_area クラスに一致する要素を特定する。
    //その後、.remove() メソッドを使用して、見つかった親要素を削除する。
  });
});

function add_artist() {
  const artist_area = $(".artist_area");
  //↑同義const artist_area = document.querySelector("#artist_area");一回めは.artist_areaが作られる前なので何も取得できない。

    // FIXME: ここでDTLは通用しない。valueの値は空にしておく
  const html = '<div class="artist_area"><input type="text" name="name" class="artist"><input type="hidden" name="edit_artist_id" value=""> <i class="fa-solid fa-xmark" style="color: gray;"></i><button class="add_song_btn" type="button" value="' + String(artist_area.length) + '">曲追加</button></div>';
  //value="' + String(artist_area.length) +'"←要素数(インデックス番号）をvalueに設定している。+ 演算子を使用して結合する必要がある。

  $(".artist_form_area").append(html);
  //#artist_form_areaの末尾にhtmlで定義された要素を追加
}

function add_song_btn(elem) {
  // elemは関数の引数であり、関数が呼び出されたときに渡される要素を表す。
  // 関数内でelemを使用すると、関数呼び出し時に渡された要素にアクセスすることができる。関数内の処理は、この要素に対して何らかの操作や処理を行うために使用される。

    // FIXME: ここでDTLは通用しない。valueの値は空にしておく
  const html = '<div class="song_area"><input type="text" name="song" class="song_item" ><input type="hidden" name="artist_id" value="' + elem.value + '"><input type="hidden" name="edit_setlist_id" value=""><i class="fa-solid fa-xmark" style="color: gray;"></i></div>';
  //artist_idはartist_areaのインデックス番号

  $(elem).parent(".artist_area").append(html);
  //引数として渡されたelem要素の親要素の中に新しい要素（htmlで定義された要素）を追加する処理を行っている
  //.parent()は、対象の要素の親要素を選択するメソッド。.artist_areaの末尾にhtmlを追加している
}
