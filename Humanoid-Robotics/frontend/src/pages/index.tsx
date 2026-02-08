import type {ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';

import styles from './index.module.css';

function HomepageHeader() {
  return (
    <header className={clsx('hero', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          AI Native Humanoid Robotics
        </Heading>
        <img
          src="/img/robot.jpg"
          alt="Robotic Arm"
          className={styles.homepageImage}
        />
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/chapter-01-introduction-to-physical-ai-robotics/intro">
            Start Reading →
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Humanoid Robotics Book`}
      description="A comprehensive guide to humanoid robotics.">
      <HomepageHeader />
    </Layout>
  );
}
