interface Props {
  Current: string;
  setCurrent: Function;
  Currentlocat: string;
  setCurrentlocat: Function;
  Position: string;
  setPosition: Function;
  FenTrans: Function;
  setPossiblemoves: Function;
  keyProp: string;
  typeS: string[];
}

function MTSquare({
  Current,
  setCurrent,
  Currentlocat,
  setCurrentlocat,
  Position,
  setPosition,
  FenTrans,
  setPossiblemoves,
  keyProp,
  typeS,
}: Props) {
  return (
    <button className={typeS[0]} onClick={getBoard}>
      <div className={typeS[1]}></div>
    </button>
  );

  function getBoard() {
    let xhr = new XMLHttpRequest();

    xhr.addEventListener("load", () => {
      let CFEN = xhr.response.slice(1, -1).split(", ").slice(1);
      CFEN[0] = CFEN[0].slice(1, -1);
      CFEN[1] = CFEN[1].slice(1, -1);
      CFEN[2] = CFEN[2].slice(1, -1);
      CFEN[3] = CFEN[3].slice(1, -1);
      CFEN[4] = +CFEN[4];
      CFEN[5] = +CFEN[5];
      CFEN[1] = CFEN[1] == "w" ? "b" : "w";
      CFEN[4] = CFEN[4] + 1;
      if (CFEN[1] == "w") {
        CFEN[5] = CFEN[5] + 1;
      }
      let Cposition = FenTrans(Position);
      let newPosition = Cposition;

      newPosition[+keyProp[0]] = newPosition[+keyProp[0]].split("");
      newPosition[+keyProp[0]][+keyProp[1]] = Current;
      newPosition[+keyProp[0]] = newPosition[+keyProp[0]].join("");

      newPosition[+Currentlocat[0]] = newPosition[+Currentlocat[0]].split("");
      newPosition[+Currentlocat[0]][+Currentlocat[1]] = ".";
      newPosition[+Currentlocat[0]] = newPosition[+Currentlocat[0]].join("");
      newPosition = newPosition.join("/");
      CFEN[0] = toFen(newPosition);
      makeMove(CFEN, newPosition);
    });

    xhr.addEventListener("error", () => {
      console.error("An error occurred while sending the request.");
    });

    let url = "http://127.0.0.1:8000/Functions/send_board";

    xhr.open("GET", url);
    xhr.send();
  }

  function makeMove(CFEN: string[], newPosition: string) {
    let xhr = new XMLHttpRequest();

    xhr.addEventListener("load", () => {
      setPosition(newPosition);
      setCurrentlocat("");
      setCurrent("");
      setPossiblemoves([""]);
    });

    xhr.addEventListener("error", () => {
      console.error("An error occurred while sending the request.");
    });

    let url = encodeURI(
      "http://127.0.0.1:8000/Functions/Set_Position/" +
        encodeURIComponent(CFEN.join(" "))
    );

    xhr.open("GET", url);
    xhr.send();
  }
}

export default MTSquare;

function toFen(position: string) {
  let newpos: string[] = [];
  let cpos = position.split("/");
  for (let x = 0; x < cpos.length; x++) {
    if (!cpos[x].includes(".")) {
      newpos.push(cpos[x]);
    } else {
      let temp = "";
      let row = cpos[x].split("");
      let count = 0;
      for (let y = 0; y < row.length; y++) {
        if (row[y] == ".") {
          count += 1;
        } else {
          if (count > 0) {
            temp += count;
          }
          temp += row[y];
          count = 0;
        }
      }
      if (count > 0) {
        temp += count;
      }
      newpos.push(temp);
    }
  }
  return newpos.join("/");
}
