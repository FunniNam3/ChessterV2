import { ReactNode } from "react";

interface Props {
  children: ReactNode;
  location: string;
}

function Box({ children, location }: Props) {
  // Return a Box with the specific class/color based on the location of the box
  return (
    <>
      {+location % 2 === 0 ? (
        <div className="Box-1">{children}</div>
      ) : (
        <div className="Box-2">{children}</div>
      )}
    </>
  );
}

export default Box;
