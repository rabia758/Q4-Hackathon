import React from 'react';
import ChapterSection from '../components/ChapterSection';

export default function Chapter1() {
  return (
    <>
      <h1>Chapter 1: Introduction</h1>

      <ChapterSection
        id="key-concepts"
        title="Key Concepts"
        concepts="Explanation of AI fundamentals..."
        examples=""
        summary=""
      />

      <ChapterSection
        id="examples"
        title="Examples"
        concepts=""
        examples="Real-world AI examples..."
        summary=""
      />

      <ChapterSection
        id="summary"
        title="Summary"
        concepts=""
        examples=""
        summary="Quick recap of the chapter..."
      />
    </>
  );
}
