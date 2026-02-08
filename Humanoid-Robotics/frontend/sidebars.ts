import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Physical AI Course',
      link: {
        type: 'doc',
        id: 'chapter-01-introduction-to-physical-ai-robotics/intro',
      },
      items: [
        'chapter-01-introduction-to-physical-ai-robotics/intro',
        'chapter-02-ros2-fundamentals/ros2',
        'chapter-03-robot-simulation/simulation',
        'chapter-04-nvidia-isaac/isaac',
        'chapter-05-humanoid-development/development',
        'chapter-06-conversational-robotics/conversational',
      ],
    },
  ],
};

export default sidebars;