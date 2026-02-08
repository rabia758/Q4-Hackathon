import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Physical AI Course',
      items: [
        'index',
        'chapter-01-introduction-to-physical-ai-robotics/index',
        'chapter-02-ros2-fundamentals/index',
        'chapter-03-robot-simulation/index',
        'chapter-04-nvidia-isaac/index',
        'chapter-05-humanoid-development/index',
        'chapter-06-conversational-robotics/index',
      ],
    },
  ],
};

export default sidebars;