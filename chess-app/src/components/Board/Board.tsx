import Box from "./Box";
import "./Board.css";
import Row from "./Row";
import Piece from "./Piece";
import MTSquare from "./Movement";
import { useState } from "react";

interface Props {
  Position: string;
  setPosition: Function;
  Possiblemoves: string[];
  setPossiblemoves: Function;
}

function Board({
  Position,
  setPosition,
  Possiblemoves,
  setPossiblemoves,
}: Props) {
  const [Current, setCurrent] = useState("");
  const [Currentlocat, setCurrentlocat] = useState("");
  // Translating the FEN position into a format that is easier to iterate through
  const TranslatedPosition = TranslateFen(Position);
  let rows = []; // Create a list to store obj rows
  // Iterate through the newly translated position
  for (let x = 0; x < TranslatedPosition.length; x++) {
    let POSrow = TranslatedPosition[x]; // Create a variable to store the current row being iterated through
    let Moverow = "";
    if (Possiblemoves.length != 1) {
      Moverow = Possiblemoves[x];
    }

    let row = []; // Variable to store the obj of a row
    // Iterate through the row to place pieces in the correct position
    for (let y = 0; y < POSrow.length; y++) {
      let BoxL = [];
      if (POSrow[y] != ".") {
        BoxL.push(
          <Piece
            key={POSrow[y]}
            piece={POSrow[y]}
            keyProp={String(x) + String(y)}
            setCurrent={setCurrent}
            setCurrentlocat={setCurrentlocat}
            setPossiblemoves={setPossiblemoves}
          ></Piece>
        );
      }
      if (Possiblemoves.length != 1) {
        if (Moverow[y] == "m") {
          BoxL.push(
            <MTSquare
              key={String(x) + String(y)}
              keyProp={String(x) + String(y)}
              Currentlocat={Currentlocat}
              setCurrentlocat={setCurrentlocat}
              setCurrent={setCurrent}
              Current={Current}
              setPosition={setPosition}
              Position={Position}
              FenTrans={TranslateFen}
              setPossiblemoves={setPossiblemoves}
              typeS={["MoveSquare", "MSdot"]}
            ></MTSquare>
          );
        } else if (Moverow[y] == "t") {
          BoxL.push(
            <MTSquare
              key={String(x) + String(y)}
              keyProp={String(x) + String(y)}
              Currentlocat={Currentlocat}
              setCurrentlocat={setCurrentlocat}
              setCurrent={setCurrent}
              Current={Current}
              setPosition={setPosition}
              Position={Position}
              FenTrans={TranslateFen}
              setPossiblemoves={setPossiblemoves}
              typeS={["MoveSquare", "TSdot"]}
            ></MTSquare>
          );
        }
      }
      row.push(
        <Box key={String(x) + String(y)} location={String(x + y)}>
          {BoxL}
        </Box>
      );
    }
    // Push the row into the list of rows
    rows.push(<Row key={x}>{row}</Row>);
  }
  // Return the Board with the rows as children
  return <div className="Board">{rows}</div>;
}
export default Board;

function TranslateFen(Fen: string) {
  const ints = [1, 2, 3, 4, 5, 6, 7, 8]; // List of integers that can be used
  let Rows = Fen.split("/"); // Split the string into a list of each row
  let newRows = []; // Create a list for translated rows to be stored
  // Iterate through all rows
  for (let x = 0; x < Rows.length; x++) {
    let row = Rows[x]; // Store the row to be iterated in a variable
    let tempRow = ""; // Create a string to store the data of each row
    // Iterate through all the items in a row
    for (let y = 0; y < row.length; y++) {
      // If the char at y is an integer
      if (ints.includes(+row[y])) {
        tempRow += ".".repeat(+row[y]); // Add the respective number of periods to the row
      } else {
        tempRow += row[y]; // Else just add the character to the temperary row
      }
    }
    newRows.push(tempRow); // Add the row to the new rows
  }
  return newRows; // return a list of the new rows
}
