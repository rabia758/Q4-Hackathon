import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import ChapterSection from '../ChapterSection';

describe('ChapterSection', () => {
  const defaultProps = {
    id: 'test-section',
    title: 'Test Chapter',
    concepts: 'Test concepts content',
    examples: 'Test examples content',
    summary: 'Test summary content',
  };

  it('renders the component with title and initial collapsed state', () => {
    render(<ChapterSection {...defaultProps} />);

    expect(screen.getByText('Test Chapter')).toBeInTheDocument();
    expect(screen.getByText('Test concepts content')).toBeInTheDocument();
    expect(screen.getByText('Test examples content')).toBeInTheDocument();
    expect(screen.getByText('Test summary content')).toBeInTheDocument();

    // Content should be hidden initially
    const content = screen.getByRole('region');
    expect(content).toHaveAttribute('aria-hidden', 'true');
  });

  it('expands and collapses when header is clicked', () => {
    render(<ChapterSection {...defaultProps} />);

    const header = screen.getByRole('button');
    expect(header).toHaveAttribute('aria-expanded', 'false');

    fireEvent.click(header);
    expect(header).toHaveAttribute('aria-expanded', 'true');
    expect(screen.getByRole('region')).toHaveAttribute('aria-hidden', 'false');

    fireEvent.click(header);
    expect(header).toHaveAttribute('aria-expanded', 'false');
    expect(screen.getByRole('region')).toHaveAttribute('aria-hidden', 'true');
  });

  it('expands and collapses with keyboard navigation', () => {
    render(<ChapterSection {...defaultProps} />);

    const header = screen.getByRole('button');
    expect(header).toHaveAttribute('aria-expanded', 'false');

    fireEvent.keyDown(header, { key: 'Enter' });
    expect(header).toHaveAttribute('aria-expanded', 'true');

    fireEvent.keyDown(header, { key: ' ' }); // Space key
    expect(header).toHaveAttribute('aria-expanded', 'false');
  });

  it('calls onToggle callback when expanded state changes', () => {
    const mockOnToggle = jest.fn();
    render(<ChapterSection {...defaultProps} onToggle={mockOnToggle} />);

    const header = screen.getByRole('button');
    fireEvent.click(header);

    expect(mockOnToggle).toHaveBeenCalledWith(true);

    fireEvent.click(header);
    expect(mockOnToggle).toHaveBeenCalledWith(false);
  });

  it('renders all three content sections (Concepts, Examples, Summary)', () => {
    render(<ChapterSection {...defaultProps} />);

    expect(screen.getByText('Concepts')).toBeInTheDocument();
    expect(screen.getByText('Examples')).toBeInTheDocument();
    expect(screen.getByText('Summary')).toBeInTheDocument();
  });

  it('accepts ReactNode content', () => {
    const reactNodeContent = <div>React node content</div>;

    render(
      <ChapterSection
        id="react-node-test"
        title="React Node Test"
        concepts={reactNodeContent}
        examples={reactNodeContent}
        summary={reactNodeContent}
      />
    );

    expect(screen.getByText('React node content')).toBeInTheDocument();
  });
});