'use client';

import { useState } from 'react';
import { Highlight, themes } from 'prism-react-renderer';

interface CodeBlockProps {
  code: string;
  language: string;
  showLineNumbers?: boolean;
}

export default function CodeBlock({
  code,
  language,
  showLineNumbers = true,
}: CodeBlockProps) {
  const [copied, setCopied] = useState(false);

  const handleCopy = async () => {
    await navigator.clipboard.writeText(code);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="code-container relative group">
      {/* Copy Button */}
      <button
        onClick={handleCopy}
        className="absolute right-4 top-4 px-3 py-1.5 text-xs font-medium text-gray-300 bg-dark-bg rounded-md opacity-0 group-hover:opacity-100 transition-opacity hover:bg-dark-border"
        aria-label="Copy code"
      >
        {copied ? (
          <span className="text-primary-400">Copied!</span>
        ) : (
          <span>Copy</span>
        )}
      </button>

      {/* Language Badge */}
      <div className="px-4 py-2 border-b border-dark-border bg-dark-bg/50">
        <span className="text-xs font-medium text-gray-400 uppercase tracking-wide">
          {language}
        </span>
      </div>

      {/* Code */}
      <Highlight theme={themes.nightOwl} code={code.trim()} language={language}>
        {({ className, style, tokens, getLineProps, getTokenProps }) => (
          <pre
            className={`${className} prism-code overflow-x-auto p-4 text-sm`}
            style={style}
          >
            {tokens.map((line, i) => (
              <div key={i} {...getLineProps({ line })}>
                {showLineNumbers && (
                  <span className="inline-block w-8 select-none text-gray-600 text-right mr-4">
                    {i + 1}
                  </span>
                )}
                {line.map((token, key) => (
                  <span key={key} {...getTokenProps({ token })} />
                ))}
              </div>
            ))}
          </pre>
        )}
      </Highlight>
    </div>
  );
}
