'use client';

import { InlineMath, BlockMath } from 'react-katex';
import 'katex/dist/katex.min.css';

interface MathBlockProps {
  equation: string;
  displayMode?: boolean;
}

export default function MathBlock({ equation, displayMode = false }: MathBlockProps) {
  if (displayMode) {
    return (
      <div className="my-6 overflow-x-auto">
        <BlockMath math={equation} />
      </div>
    );
  }

  return <InlineMath math={equation} />;
}
