import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Course Overview',
      link: {
        type: 'doc',
        id: 'chapter-01-introduction-to-physical-ai-robotics/index',
      },
      items: [
        'chapter-01-introduction-to-physical-ai-robotics/index',
        'chapter-02-mathematics-for-robotics/index',
        'chapter-03-robot-kinematics/index',
        'chapter-04-robot-dynamics/index',
        'chapter-05-sensors-for-humanoid-robotics/index',
      ],
    },
  ],
};

export default sidebars;
