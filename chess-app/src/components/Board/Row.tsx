import { ReactNode } from "react";

interface Props {
  children: ReactNode;
}

function Row({ children }: Props) {
  // Returns the row
  return <div className="Row">{children}</div>;
}

export default Row;
