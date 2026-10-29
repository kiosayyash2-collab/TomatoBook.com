<<!DOCTYPE <html>
    <<body>

      <h1>input username</h1>
    
      <<form action="showdata.php" method="POST">>
        <<label for="username">Enter you name</label>><br>
        <<input type="text" name="text" value="username">>
        <br>

        <<label for="userage">Enter you age</label>><br>
        <<input type="num" name="num" value="userage">>
        <br>

        <<input type="submit" name="submit" value="save">>
        <br>
      </form>

    </body>
    <<script>
      let username;
      //username function
      document.getElementById("mysubmit").onclick = function(){
        null;
      }
    </script>
</html>>
